<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Mini Java Compiler + AST Viewer</title>

<style>
body {
  margin: 0;
  font-family: monospace;
  background: #0b0f1a;
  color: white;
}

.container {
  display: flex;
  height: 100vh;
}

textarea {
  width: 40%;
  background: #050814;
  color: white;
  border: none;
  padding: 10px;
  outline: none;
}

.right {
  width: 60%;
  display: flex;
  flex-direction: column;
}

.output {
  flex: 1;
  padding: 10px;
  overflow: auto;
  background: #050814;
}

.ast {
  flex: 1;
  padding: 10px;
  overflow: auto;
  border-top: 1px solid #1e3a5f;
  background: #070b18;
}

button {
  margin: 5px;
  padding: 6px;
  background: #12223a;
  color: white;
  border: 1px solid #1e3a5f;
  cursor: pointer;
}

.node {
  margin-left: 15px;
}
</style>
</head>

<body>

<div class="container">

<textarea id="code">
class Main {

  function main() {
    int x = 5;
    int y = 10;

    if (x < y) {
      System.out.println("x is smaller");
    }

    while (x < 8) {
      x = x + 1;
      System.out.println(x);
    }

    for (int i = 0; i < 3; i = i + 1) {
      System.out.println(i);
    }
  }
}
</textarea>

<div class="right">

<div>
<button onclick="run()">Run</button>
<button onclick="step()">Step Debug</button>
</div>

<div class="output" id="out"></div>
<div class="ast" id="ast"></div>

</div>
</div>

<script>

/* =========================
   1. LEXER (TOKENIZER)
========================= */
function tokenize(code) {
  return code
    .replace(/([{}();=<>+\-*/])/g, " $1 ")
    .split(/\s+/)
    .filter(t => t.length);
}

/* =========================
   2. AST NODE
========================= */
class Node {
  constructor(type, value = null, children = []) {
    this.type = type;
    this.value = value;
    this.children = children;
  }
}

/* =========================
   3. PARSER (VERY SIMPLIFIED)
========================= */
function parse(tokens) {
  let i = 0;

  function peek() { return tokens[i]; }
  function eat() { return tokens[i++]; }

  function parseBlock() {
    let nodes = [];

    while (i < tokens.length && peek() !== "}") {
      nodes.push(parseStmt());
    }

    if (peek() === "}") eat();
    return nodes;
  }

  function parseStmt() {

    let t = peek();

    // function
    if (t === "function") {
      eat();
      let name = eat();
      eat(); // (
      eat(); // )
      eat(); // {

      let body = parseBlock();
      return new Node("function", name, body);
    }

    // if
    if (t === "if") {
      eat();
      eat(); // (
      let cond = eat() + eat() + eat();
      eat(); // )
      eat(); // {

      let body = parseBlock();
      return new Node("if", cond, body);
    }

    // while
    if (t === "while") {
      eat();
      eat();
      let cond = eat() + eat() + eat();
      eat();
      let body = parseBlock();
      return new Node("while", cond, body);
    }

    // class (convert to object later)
    if (t === "class") {
      eat();
      let name = eat();
      eat(); // {

      let body = parseBlock();
      return new Node("class", name, body);
    }

    // expression
    let expr = [];
    while (peek() && peek() !== ";") {
      expr.push(eat());
    }
    eat(); // ;
    return new Node("expr", expr.join(" "));
  }

  return parseBlock();
}

/* =========================
   4. EXECUTOR
========================= */
let env = {};
let ast = [];
let pc = 0;

function evalExpr(expr) {
  try {
    return Function("env", "with(env){return " + expr + "}")(env);
  } catch {
    return expr;
  }
}

function execNode(node) {

  if (!node) return;

  if (node.type === "expr") {

    if (node.value.includes("System.out.println")) {
      let v = node.value.replace("System.out.println", "").replace(/[()]/g, "");
      log(evalExpr(v));
    } else {
      Function("env", "with(env){" + node.value + "}")(env);
    }
  }

  if (node.type === "if") {
    if (evalExpr(node.value)) {
      node.children.forEach(execNode);
    }
  }

  if (node.type === "while") {
    while (evalExpr(node.value)) {
      node.children.forEach(execNode);
    }
  }

  if (node.type === "function") {
    env[node.value] = () => node.children.forEach(execNode);
  }

  if (node.type === "class") {
    env[node.value] = {};
    node.children.forEach(n => {
      if (n.type === "function") {
        env[node.value][n.value] = () => n.children.forEach(execNode);
      }
    });
  }
}

/* =========================
   5. RUN
========================= */
function run() {
  document.getElementById("out").innerHTML = "";
  document.getElementById("ast").innerHTML = "";

  env = {};

  let code = document.getElementById("code").value;
  let tokens = tokenize(code);
  ast = parse(tokens);

  renderAST(ast);
  ast.forEach(execNode);
}

/* =========================
   6. DEBUG STEP
========================= */
function step() {
  if (pc < ast.length) {
    execNode(ast[pc]);
    pc++;
  }
}

/* =========================
   7. OUTPUT
========================= */
function log(x) {
  document.getElementById("out").innerHTML += x + "<br>";
}

/* =========================
   8. AST VIEWER
========================= */
function renderAST(nodes, depth = 0, parent = document.getElementById("ast")) {

  nodes.forEach(n => {
    let div = document.createElement("div");
    div.className = "node";
    div.style.marginLeft = depth * 15 + "px";
    div.textContent = n.type + " : " + (n.value || "");
    parent.appendChild(div);

    if (n.children) renderAST(n.children, depth + 1, parent);
  });
}

</script>

</body>
</html>