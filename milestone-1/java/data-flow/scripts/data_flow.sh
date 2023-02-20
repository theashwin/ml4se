#!/bin/bash

echo 'digraph {
	start -> a;
	a -> try1;
	try1 -> b;
	b -> c;
	try1 -> except1;
	except1 -> d;
	d -> end;
	c -> try2;
	try2 -> e;
	e -> end;
	try2 -> except2;
	except2 -> f;
	f -> end;

	a [shape=box, label="makefile = get_makefile_filename(...)"]	
	b [shape=box, label = "_parse_makefile(makefile, ...)"]
	c [shape=box, label = "config_h = get_config_h_filename(...)"]
	d [shape=box, label = "msg = ... % makefile"]
	e [shape=box, label = "open(config_h)"]
	f [shape=box, label = "msg = ... % config_h"]
	# if1 [shape=diamond, label="if"]
	# else1 [shape=diamond, label="else1"]
	# if3 [shape=diamond, label="if3"]

}' | dot -Tsvg > 71.svg