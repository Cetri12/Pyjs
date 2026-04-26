<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Java → JS Transpiler</title>

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
  padding: 10px;
  background: #050814;
  overflow-y: auto;
  white-space: pre-wrap;
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
<button onclick="compileRun()">Compile + Run</button>
<button onclick="clearOut()">Clear</button>
</div>

<div class="container">
<textarea id="java">
public class Main {
    public static void main(String[] args) {

        int x = 5;
        int y = 10;

        System.out.println(x + y);

        String name = "Alice";
        System.out.println(name);

        var list = [];
        list.push(1);
        list.push(2);
        System.out.println(list);
    }
}
</textarea>

<div class="output" id="out"></div>
</div>

<script>

/* ---------------- OUTPUT ---------------- */
function log(x) {
  document.getElementById("out").textContent += x + "\n";
}

/* ---------------- TRANSPILER ---------------- */
function javaToJS(java) {

  let js = java;

  // remove class wrapper
  js = js.replace(/public class.*?\\{/, "");
  js = js.replace(/\\}$/, "");

  // main method removal
  js = js.replace(/public static void main.*?\\{/, "");

  // System.out.println → console.log
  js = js.replace(/System\\.out\\.println/g, "log");

  // int / String / var → let
  js = js.replace(/\\b(int|String|var|double|float|boolean)\\b/g, "let");

  // ArrayList → []
  js = js.replace(/new ArrayList<.*?>\\(\\)/g, "[]");

  // .add → .push
  js = js.replace(/\\.add/g, ".push");

  return js;
}

/* ---------------- RUN ---------------- */
function compileRun() {
  document.getElementById("out").textContent = "";

  const javaCode = document.getElementById("java").value;

  const jsCode = javaToJS(javaCode);

  try {
    const fn = new Function("log", jsCode);
    fn(log);
  } catch (e) {
    log("Error: " + e.message);
  }
}

/* ---------------- CLEAR ---------------- */
function clearOut() {
  document.getElementById("out").textContent = "";
}

</script>

</body>
</html>