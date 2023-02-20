#!/bin/bash

echo 'digraph {
	start -> a;
	# while -> a;
	# while -> end;
	a -> end
	# a -> if;
	# if -> b;
	# if -> c;
	# b -> c;
	# b-> end;
	# a -> end;

	a [shape=box, label="columnMetadataList = getColumns(...)"]	
	# b [shape=box, label="lastCommitTime = nanoTime(...)"]
}' | dot -Tsvg > CdcSourcePresolveMappingColumns.svg
