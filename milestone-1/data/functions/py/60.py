def target(self, project_module):
        """Returns the project target corresponding to the 'project-module'."""
        assert isinstance(project_module, basestring)
        if project_module not in self.module2target:
            self.module2target[project_module] = \
                b2.build.targets.ProjectTarget(project_module, project_module,
                              self.attribute(project_module, "requirements"))

        return self.module2target[project_module]