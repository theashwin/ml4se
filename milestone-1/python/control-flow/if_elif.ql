import python

from Function f, Stmt stmt, If iff
where f.getLocation().getFile() = stmt.getLocation().getFile() and
iff = stmt and
stmt instanceof If
select
f.getLocation().getFile().toString() as File,
iff.getBody().getItem(0).getLocation().toString() as BodyLocation,
iff.getElif().getBody().getItem(0).getLocation().toString() as ElIf,
iff.getLastStatement().getLocation().toString() as LastStatementForIf