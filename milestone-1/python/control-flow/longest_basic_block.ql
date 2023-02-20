import python

int bb_length(BasicBlock b) {
    result = max(int i | exists(b.getNode(i)) | i) + 1
}

from Function f, BasicBlock b
where f.getLocation().getFile() = b.getNode(0).getLocation().getFile()
select f.getLocation().getFile().toString(), b, b.getNode(0).getLocation(), b.getLastNode().getLocation()
