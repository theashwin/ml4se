#!/bin/bash

echo 'digraph {
	start -> if1;
	if1 -> a;
	a -> if2;
	if2 -> b;
	b -> c;
	if2 -> c;
	c -> d;
	if1 -> d;

	b [shape=box, label="result = startsWith(...)"]	
	# b [shape=box, label = "snapshotTraverser = onFirstNull(...)"]
	# e [shape=box, label = "queries = new Queries(...)"]
	# f [shape=box, label = "initFailure = e"]
	# if [shape=diamond, label="if"]
	# if2 [shape=diamond, label="if2"]
	# if3 [shape=diamond, label="if3"]

}' | dot -Tsvg > GenericMapStoreisIntegrityConstraintViolation.svg