<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Hybrid Python + JS Interpreter</title>

<style>
body {
  margin: 0;
  font-family: monospace;
  background: #0b0f1a;
  color: white;
}

.header {
  padding: 10px;
  background: #050814;
  border-bottom: 1px solid #1e3a5f;
}

.container {
  display: flex;
  height: calc(100vh - 50px);
}

textarea {
  width: 50%;
  height: 100%;
  background: #050814;
  color: white;
  border: none;
  padding: 10px;
  resize: none;
  outline: none;
}

.output {
  width: 50%;
  background: #050814;
  padding: 10px;
  overflow-y: auto;
  white-space: pre-wrap;
}

.output::before {
  content: "OUTPUT";
  display: block;
  color: #4aa3ff;
  font-weight: bold;
  margin-bottom: 10px;
}

#inputBox {
  width: 100%;
  margin-top: 10px;
  padding: 8px;
  background: #0b0f1a;
  color: white;
  border: 1px solid #1e3a5f;
}

button {
  margin: 5px;
  background: #12223a;
  color: white;
  border: 1px solid #1e3a5f;
  padding: 5px 10px;
  cursor: pointer;
}
</style>
</head>

<body>

<div class="header">
<button onclick="run()">Run</button>
<button onclick="clearOut()">Clear</button>
<button onclick="downloadHTML()">Download HTML</button>
<button onclick="downloadJS()">Download JS</button>
</div>

<div class="container">
<textarea id="code">
def demo():
    x = 5
    y = js("return x * 2")
    print(y)

    js("log('JS sees x = ' + x)")

    nums = [1,2,3]
    js("nums.push(99)")
    print(nums)

demo()
</textarea>

<div class="output">
<div id="output"></div>
<input id="inputBox" placeholder="Type input + Enter">
</div>
</div>

<script>

/* ---------------- INPUT ---------------- */
let inputResolver = null;

document.getElementById("inputBox").addEventListener("keydown", e => {
  if (e.key === "Enter") {
    let v = e.target.value;
    e.target.value = "";
    if (inputResolver) {
      inputResolver(v);
      inputResolver = null;
    }
  }
});

function input(promptText) {
  log(promptText);
  return new Promise(res => inputResolver = res);
}

/* ---------------- OUTPUT ---------------- */
function log(x) {
  document.getElementById("output").textContent += x + "\\n";
}

/* ---------------- SAFE JS BRIDGE ---------------- */
function runJS(code, env) {
  const safeAPI = {
    log,
    Math,
    Number,
    String,
    Array
  };

  return Function("env", "api", `
    const { log, Math, Number, String, Array } = api;
    with(env) {
      return (function(){
        ${code}
      })();
    }
  `)(env, safeAPI);
}

/* ---------------- AST ---------------- */
class Node {
  constructor(type, value = null, children = []) {
    this.type = type;
    this.value = value;
    this.children = children;
  }
}

/* ---------------- PARSER ---------------- */
function parse(lines, indent = 0, i = {v:0}) {
  let nodes = [];

  while (i.v < lines.length) {
    let line = lines[i.v];
    if (!line.trim()) { i.v++; continue; }

    let curIndent = line.match(/^ */)[0].length;
    if (curIndent < indent) break;

    line = line.trim();

    if (line.startsWith("def ")) {
      let name = line.split("def ")[1].split("(")[0].trim();
      i.v++;
      let body = parse(lines, curIndent + 4, i);
      nodes.push(new Node("func", name, body));
    }

    else if (line.startsWith("if ")) {
      let cond = line.slice(3, -1);
      i.v++;
      let body = parse(lines, curIndent + 4, i);
      nodes.push(new Node("if", cond, body));
    }

    else if (line.startsWith("for ")) {
      let v = line.split("for ")[1].split(" in")[0].trim();
      let n = line.match(/range\\((\\d+)\\)/)[1];
      i.v++;
      let body = parse(lines, curIndent + 4, i);
      nodes.push(new Node("for", {v, n}, body));
    }

    else {
      nodes.push(new Node("stmt", line));
      i.v++;
    }
  }

  return nodes;
}

/* ---------------- EXECUTOR ---------------- */
async function exec(nodes, env = {}) {

  for (let n of nodes) {

    if (n.type === "func") {
      env[n.value] = async () => await exec(n.children, env);
    }

    else if (n.type === "if") {
      if (evalExpr(n.value, env)) {
        await exec(n.children, env);
      }
    }

    else if (n.type === "for") {
      for (let i = 0; i < n.value.n; i++) {
        env[n.value.v] = i;
        await exec(n.children, env);
      }
    }

    else if (n.type === "stmt") {
      await runStmt(n.value, env);
    }
  }
}

/* ---------------- STATEMENTS ---------------- */
async function runStmt(line, env) {

  if (line.startsWith("print(")) {
    let v = line.slice(6, -1);
    log(evalExpr(v, env));
  }

  else if (line.includes("input(")) {
    let name = line.split("=")[0].trim();
    let prompt = line.match(/input\\((.*)\\)/);
    let p = prompt ? eval(prompt[1]) : "";
    env[name] = await input(p);
  }

  else if (line.startsWith("js(")) {
    let code = line.slice(3, -1);
    runJS(code, env);
  }

  else if (line.includes(".append")) {
    let list = line.split(".append")[0].trim();
    let val = line.match(/\\.append\\((.*)\\)/)[1];
    env[list].push(evalExpr(val, env));
  }

  else if (line.includes("=")) {
    let [l, r] = line.split("=");

    if (r.trim().startsWith("js(")) {
      let code = r.trim().slice(3, -1);
      env[l.trim()] = runJS(code, env);
    } else {
      env[l.trim()] = evalExpr(r.trim(), env);
    }
  }
}

/* ---------------- EXPRESSIONS ---------------- */
function evalExpr(expr, env) {
  try {
    return Function("env", "with(env){return " + expr + "}")(env);
  } catch {
    return expr;
  }
}

/* ---------------- RUN ---------------- */
async function run() {
  document.getElementById("output").textContent = "";
  const code = document.getElementById("code").value;
  const lines = code.split("\\n");
  const ast = parse(lines, 0, {v:0});
  await exec(ast, {});
}

/* ---------------- CLEAR ---------------- */
function clearOut() {
  document.getElementById("output").textContent = "";
}

/* ---------------- DOWNLOAD JS ---------------- */
function downloadJS() {
  const code = document.getElementById("code").value;
  const blob = new Blob([code], { type: "text/javascript" });
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = "script.js";
  a.click();
}

/* ---------------- DOWNLOAD HTML ---------------- */
function downloadHTML() {
  const code = document.getElementById("code").value;

  const template = `<!DOCTYPE html>
<html>
<body>
<pre id="out"></pre>
<script>
function log(x){document.getElementById("out").textContent += x + "\\n";}
${runJS.toString()}
let env = {};
runJS(\`
${code}
\`, env);
<\/script>
</body>
</html>`;

  const blob = new Blob([template], { type: "text/html" });
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = "program.html";
  a.click();
}

</script>

</body>
</html>