import python

// AugAssign
from Function func, Stmt stmt, AugAssign aug
where
(stmt instanceof AugAssign) and
not (aug.getParentNode() instanceof If) and
aug = stmt and
stmt.getLocation().getFile() = func.getLocation().getFile()
//LOCATION OF PARENT IF, LOCATION OF STMT, LEFT ASSIGMENT, RIGHT ASSIGNMENT
select aug.getParentNode().getLocation(), stmt.getLocation(), aug.getTarget(), aug.getAChildNode()
