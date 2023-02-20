import python

// AssignStmt - Tuple
from Function func, Stmt stmt, AssignStmt ass
where
(stmt instanceof AssignStmt) and
ass = stmt and
not (ass.getParentNode() instanceof If) and
stmt.getLocation().getFile() = func.getLocation().getFile() and
ass.getTargets().getAnItem().getLocation() = ass.getAChildNode().getLocation() and
ass.getTargets().getAnItem() instanceof Tuple and
not (ass.getTargets().getAnItem().getAChildNode() = ass.getAChildNode())
// LOCATION OF PARENT IF, LOCATION OF STMT, LEFT ASSIGMENT, RIGHT ASSIGNMENT
select ass.getParentNode().getLocation().toString(), stmt.getLocation().toString(), ass.getTargets().getAnItem().getAChildNode().toString(), ass.getAChildNode().toString(), ass.getAChildNode()
