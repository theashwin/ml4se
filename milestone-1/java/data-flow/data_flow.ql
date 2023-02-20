// Java Data Flow
import java
from Class targetClass, Method func, Expr stmt, Assignment ass
where
(
  targetClass.hasName("HazelcastManifestTransformer")
  or
  targetClass.hasName("CdcSourceP")
  or
  targetClass.hasName("GenericMapStore")
)
and
func.getFile() = targetClass.getFile()
and
stmt.getFile() = targetClass.getFile()
and
stmt.getEnclosingCallable() = func
and
ass.getEnclosingCallable() = func
and
func.toString() != "<obinit>"
and
func.toString() != "<clinit>"
and
stmt instanceof Assignment
and
ass = stmt
select 
targetClass.toString() as targetJavaClass, 
func.toString() as funcName,
ass.getSource().toString() as source,
ass.getDest().toString() as dest,
stmt.getBasicBlock().getEnclosingStmt().getParent().toString() as assignmentParent,
ass.getSource().getType().toString() as sourceType,
ass.getDest().getType().toString() as destType