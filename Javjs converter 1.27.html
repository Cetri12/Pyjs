<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Level 3 Java IDE (Mini Compiler)</title>

<style>
body {
  margin: 0;
  font-family: monospace;
  background: #0b0f1a;
  color: #e6f1ff;
}

.container {
  display: flex;
  height: 100vh;
}

/* EDITOR */
#code {
  width: 40%;
  background: #050814;
  color: white;
  padding: 10px;
  border: none;
  outline: none;
}

/* RIGHT PANEL */
.right {
  width: 60%;
  display: flex;
  flex-direction: column;
}

.toolbar {
  background: #0a1224;
  padding: 6px;
}

button {
  margin: 3px;
  padding: 5px;
  background: #12223a;
  color: white;
  border: 1px solid #1e3a5f;
  cursor: pointer;
}

#output {
  flex: 1;
  padding: 10px;
  overflow: auto;
  background: #050814;
}

#ast {
  flex: 1;
  padding: 10px;
  overflow: auto;
  background: #070b18;
  border-top: 1px solid #1e3a5f;
}

.node {
  margin-left: 12px;
  cursor: pointer;
  color: #79c0ff;
}

.vars {
  padding: 10px;
  border-top: 1px solid #1e3a5f;
  background: #050814;
  height: 150px;
  overflow: auto;
}
</style>
</head>

<body>

<div class="container">

<textarea id="code">
class Main {

  function add(a, b) {
    return a + b;
  }

  function main() {

    let x = 10;
    let y = 20;

    let z = add(x, y);
    System.out.println(z);

    if (z > 20) {
      System.out.println("big");
    }

    let i = 0;
    while (i < 3) {
      System.out.println(i);
      i = i + 1;
    }
  }
}
</textarea>

<div class="right">

<div class="toolbar">
<button onclick="run()">Run</button>
<button onclick="step()">Step</button>
<button onclick="reset()">Reset</button>
</div>

<div id="output"></div>
<div id="ast"></div>
<div class="vars" id="vars"></div>

</div>
</div>

<script>

/* =========================
   LEXER (REAL TOKENIZER)
========================= */
function tokenize(input) {
  let tokens = [];
  let current = "";

  for (let c of input) {

    if ("{}();=+-*/<>,".includes(c)) {
      if (current) tokens.push(current), current = "";
      tokens.push(c);
    }
    else if (c === " " || c === "\n") {
      if (current) tokens.push(current), current = "";
    }
    else {
      current += c;
    }
  }

  if (current) tokens.push(current);
  return tokens;
}

/* =========================
   AST NODE
========================= */
class Node {
  constructor(type, value = null, children = []) {
    this.type = type;
    this.value = value;
    this.children = children;
  }
}

/* =========================
   PARSER (SIMPLIFIED REAL)
========================= */
function parse(tokens) {
  let i = 0;

  function peek() { return tokens[i]; }
  function eat() { return tokens[i++]; }

  function parseBlock() {
    let nodes = [];
    while (peek() && peek() !== "}") {
      nodes.push(parseStmt());
    }
    eat(); // }
    return nodes;
  }

  function parseExpr() {
    let expr = [];
    while (peek() && peek() !== ";" && peek() !== ")") {
      expr.push(eat());
    }
    return expr.join(" ");
  }

  function parseStmt() {

    if (peek() === "class") {
      eat();
      let name = eat();
      eat(); // {
      return new Node("class", name, parseBlock());
    }

    if (peek() === "function") {
      eat();
      let name = eat();
      eat(); // (
      let args = [];
      while (peek() !== ")") args.push(eat());
      eat(); eat(); // ) {

      return new Node("function", { name, args }, parseBlock());
    }

    let expr = parseExpr();
    eat(); // ;
    return new Node("expr", expr);
  }

  return parseBlock();
}

/* =========================
   RUNTIME (STACK + SCOPE)
========================= */
let envStack = [{}];
let ast = [];
let pc = 0;

function env() {
  return envStack[envStack.length - 1];
}

function pushEnv(obj = {}) {
  envStack.push(obj);
}

function popEnv() {
  envStack.pop();
}

/* =========================
   EVALUATOR
========================= */
function evalExpr(expr) {
  try {
    return Function("env", "with(env){return " + expr + "}")(env());
  } catch {
    return undefined;
  }
}

/* =========================
   EXECUTOR
========================= */
function exec(node) {

  if (node.type === "expr") {

    if (node.value.includes("System.out.println")) {
      let v = node.value.replace("System.out.println", "").replace(/[()]/g, "");
      log(evalExpr(v));
    }

    else if (node.value.includes("=")) {
      let [l, r] = node.value.split("=");
      env()[l.trim()] = evalExpr(r.trim());
    }
  }

  if (node.type === "function") {
    env()[node.value.name] = (...args) => {
      pushEnv({});
      node.value.args.forEach((a, i) => env()[a] = args[i]);
      node.children.forEach(exec);
      popEnv();
    };
  }

  if (node.type === "class") {
    env()[node.value] = {};
    node.children.forEach(n => {
      if (n.type === "function") {
        env()[node.value][n.value.name] = (...args) => {
          pushEnv({});
          n.value.args.forEach((a, i) => env()[a] = args[i]);
          n.children.forEach(exec);
          popEnv();
        };
      }
    });
  }
}

/* =========================
   DEBUG ENGINE
========================= */
function run() {
  document.getElementById("output").innerHTML = "";
  document.getElementById("ast").innerHTML = "";
  document.getElementById("vars").innerHTML = "";

  envStack = [{}];
  pc = 0;

  const code = document.getElementById("code").value;
  const tokens = tokenize(code);
  ast = parse(tokens);

  renderAST(ast);
  ast.forEach(exec);
}

/* STEP DEBUG */
function step() {
  if (pc < ast.length) {
    exec(ast[pc]);
    pc++;
    renderVars();
  }
}

/* RESET */
function reset() {
  envStack = [{}];
  pc = 0;
  document.getElementById("output").innerHTML = "";
}

/* =========================
   OUTPUT
========================= */
function log(x) {
  document.getElementById("output").innerHTML += x + "<br>";
}

/* =========================
   AST VIEWER
========================= */
function renderAST(nodes, depth = 0) {
  let astDiv = document.getElementById("ast");

  nodes.forEach(n => {
    let div = document.createElement("div");
    div.className = "node";
    div.style.marginLeft = depth * 15 + "px";
    div.textContent = n.type + " → " + (n.value?.name || n.value);
    astDiv.appendChild(div);

    if (n.children) renderAST(n.children, depth + 1);
  });
}

/* =========================
   VARIABLE INSPECTOR
========================= */
function renderVars() {
  let v = document.getElementById("vars");
  v.innerHTML = "<b>Variables:</b><br>";

  envStack.forEach((scope, i) => {
    v.innerHTML += "<br>Scope " + i + ":<br>";
    v.innerHTML += JSON.stringify(scope, null, 2) + "<br>";
  });
}

</script>

</body>
</html>