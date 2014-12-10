--- lsystems.py	(original)
+++ lsystems.py	(refactored)
@@ -91,7 +91,7 @@
 py_version = sys.version_info[:2]
 if py_version < (2,6):
    print("This program requires Python version 2.6 or greater to run.")
-   print("Your version of Python is " + '.'.join(map(str,py_version)) + ", which is too old.")
+   print(("Your version of Python is " + '.'.join(map(str,py_version)) + ", which is too old."))
    sys.exit(-1)
 
 # Some demo functions, which make it relatively easy to use
@@ -100,7 +100,7 @@
    def show_demo(name, action):
       print(name)
       action()
-      input = raw_input("Press any key to continue or q/Q to quit: ")
+      input = input("Press any key to continue or q/Q to quit: ")
       if input.lower() == 'q':
          sys.exit(0)
    show_demo("Bushy tree", demo1)
@@ -237,9 +237,9 @@
    def __init__ (self, rules):
       if len(rules) > 0:
          for r in rules:
-            exec(compile(r)) in locals()
+            exec((compile(r)), locals())
          firstRuleName,_ = decomposeRule(rules[0])
-         exec('def start(n): return ' + firstRuleName + '(n)') in locals()
+         exec(('def start(n): return ' + firstRuleName + '(n)'), locals())
          self.rule = start
       else:
          self.rule = lambda _ : ''
@@ -258,7 +258,7 @@
       def action_fun(token):
          return self.actions.get(token, lambda _ : None)(self)
       self.stack = deque() 
-      map (action_fun, tokens)
+      list(map (action_fun, tokens))
 
    def push(self):
       orient = heading()
@@ -327,9 +327,9 @@
    ifBody = varBinds + ['return ' + joinListPart]
    elsePart = 'else: return ' + quote(name)
    return '\n'.join(
-      [defPart] + map(indent,
-         [ifHead] + map(indent,
-            ifBody) + [elsePart]))
+      [defPart] + list(map(indent,
+         [ifHead] + list(map(indent,
+            ifBody)) + [elsePart])))
 
 def decomposeRule(rule):
    splitRule = rule.split('->')
