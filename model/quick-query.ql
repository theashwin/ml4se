// Java Control Flow
import java
from Class targetClass, Method func, Stmt stmt
where
(
  targetClass.hasName("HazelcastManifestTransformer")
  or
  targetClass.hasName("CdcSourceP")
)
and
func.getFile() = targetClass.getFile()
and
stmt.getFile() = targetClass.getFile()
and
stmt.getEnclosingCallable() = func
and
stmt instanceof IfStmt 
select targetClass.toString() as targetJavaClass, 
func.toString() as funcName, 
stmt.getLocation().toString() as statementLocation, 
stmt.toString() as stmtType, 
stmt.getEnclosingStmt().getParent().toString() as parentOfStmt