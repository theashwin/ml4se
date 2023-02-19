def setup_default_layouts(self, index, settings):
        """Setup default layouts when run for the first time."""
        self.setUpdatesEnabled(False)

        first_spyder_run = bool(self.first_spyder_run)  # Store copy

        if first_spyder_run:
            self.set_window_settings(*settings)
        else:
            if self.last_plugin:
                if self.last_plugin.ismaximized:
                    self.maximize_dockwidget(restore=True)

            if not (self.isMaximized() or self.maximized_flag):
                self.showMaximized()

            min_width = self.minimumWidth()
            max_width = self.maximumWidth()
            base_width = self.width()
            self.setFixedWidth(base_width)

        # IMPORTANT: order has to be the same as defined in the config file
        MATLAB, RSTUDIO, VERTICAL, HORIZONTAL = range(self.DEFAULT_LAYOUTS)

        # Define widgets locally
        editor = self.editor
        console_ipy = self.ipyconsole
        console_int = self.console
        outline = self.outlineexplorer
        explorer_project = self.projects
        explorer_file = self.explorer
        explorer_variable = self.variableexplorer
        plots = self.plots
        history = self.historylog
        finder = self.findinfiles
        help_plugin = self.help
        helper = self.onlinehelp
        plugins = self.thirdparty_plugins

        # Stored for tests
        global_hidden_widgets = [finder, console_int, explorer_project,
                                 helper] + plugins
        global_hidden_toolbars = [self.source_toolbar, self.edit_toolbar,
                                  self.search_toolbar]
        # Layout definition
        # --------------------------------------------------------------------
        # Layouts are organized by columns, each column is organized by rows.
        # Widths have to add 1.0 (except if hidden), height per column has to
        # add 1.0 as well

        # Spyder Default Initial Layout
        s_layout = {
            'widgets': [
                # Column 0
                [[explorer_project]],
                # Column 1
                [[editor]],
                # Column 2
                [[outline]],
                # Column 3
                [[help_plugin, explorer_variable, plots,     # Row 0
                  helper, explorer_file, finder] + plugins,
                 [console_int, console_ipy, history]]        # Row 1
                ],
            'width fraction': [0.05,            # Column 0 width
                               0.55,            # Column 1 width
                               0.05,            # Column 2 width
                               0.45],           # Column 3 width
            'height fraction': [[1.0],          # Column 0, row heights
                                [1.0],          # Column 1, row heights
                                [1.0],          # Column 2, row heights
                                [0.46, 0.54]],  # Column 3, row heights
            'hidden widgets': [outline] + global_hidden_widgets,
            'hidden toolbars': [],
        }

        # RStudio
        r_layout = {
            'widgets': [
                # column 0
                [[editor],                            # Row 0
                 [console_ipy, console_int]],         # Row 1
                # column 1
                [[explorer_variable, plots, history,  # Row 0
                  outline, finder] + plugins,
                 [explorer_file, explorer_project,    # Row 1
                  help_plugin, helper]]
                ],
            'width fraction': [0.55,            # Column 0 width
                               0.45],           # Column 1 width
            'height fraction': [[0.55, 0.45],   # Column 0, row heights
                                [0.55, 0.45]],  # Column 1, row heights
            'hidden widgets': [outline] + global_hidden_widgets,
            'hidden toolbars': [],
        }

        # Matlab
        m_layout = {
            'widgets': [
                # column 0
                [[explorer_file, explorer_project],
                 [outline]],
                # column 1
                [[editor],
                 [console_ipy, console_int]],
                # column 2
                [[explorer_variable, plots, finder] + plugins,
                 [history, help_plugin, helper]]
                ],
            'width fraction': [0.10,            # Column 0 width
                               0.45,            # Column 1 width
                               0.45],           # Column 2 width
            'height fraction': [[0.55, 0.45],   # Column 0, row heights
                                [0.55, 0.45],   # Column 1, row heights
                                [0.55, 0.45]],  # Column 2, row heights
            'hidden widgets': global_hidden_widgets,
            'hidden toolbars': [],
        }

        # Vertically split
        v_layout = {
            'widgets': [
                # column 0
                [[editor],                                  # Row 0
                 [console_ipy, console_int, explorer_file,  # Row 1
                  explorer_project, help_plugin, explorer_variable, plots,
                  history, outline, finder, helper] + plugins]
                ],
            'width fraction': [1.0],            # Column 0 width
            'height fraction': [[0.55, 0.45]],  # Column 0, row heights
            'hidden widgets': [outline] + global_hidden_widgets,
            'hidden toolbars': [],
        }

        # Horizontally split
        h_layout = {
            'widgets': [
                # column 0
                [[editor]],                                 # Row 0
                # column 1
                [[console_ipy, console_int, explorer_file,  # Row 0
                  explorer_project, help_plugin, explorer_variable, plots,
                  history, outline, finder, helper] + plugins]
                ],
            'width fraction': [0.55,      # Column 0 width
                               0.45],     # Column 1 width
            'height fraction': [[1.0],    # Column 0, row heights
                                [1.0]],   # Column 1, row heights
            'hidden widgets': [outline] + global_hidden_widgets,
            'hidden toolbars': []
        }

        # Layout selection
        layouts = {
            'default': s_layout,
            RSTUDIO: r_layout,
            MATLAB: m_layout,
            VERTICAL: v_layout,
            HORIZONTAL: h_layout,
        }

        layout = layouts[index]

        # Remove None from widgets layout
        widgets_layout = layout['widgets']
        widgets_layout_clean = []
        for column in widgets_layout:
            clean_col = []
            for row in column:
                clean_row = [w for w in row if w is not None]
                if clean_row:
                    clean_col.append(clean_row)
            if clean_col:
                widgets_layout_clean.append(clean_col)

        # Flatten widgets list
        widgets = []
        for column in widgets_layout_clean:
            for row in column:
                for widget in row:
                    widgets.append(widget)

        # Make every widget visible
        for widget in widgets:
            widget.toggle_view(True)
            widget.toggle_view_action.setChecked(True)

        # We use both directions to ensure proper update when moving from
        # 'Horizontal Split' to 'Spyder Default'
        # This also seems to help on random cases where the display seems
        # 'empty'
        for direction in (Qt.Vertical, Qt.Horizontal):
            # Arrange the widgets in one direction
            for idx in range(len(widgets) - 1):
                first, second = widgets[idx], widgets[idx+1]
                if first is not None and second is not None:
                    self.splitDockWidget(first.dockwidget, second.dockwidget,
                                         direction)

        # Arrange the widgets in the other direction
        for column in widgets_layout_clean:
            for idx in range(len(column) - 1):
                first_row, second_row = column[idx], column[idx+1]
                self.splitDockWidget(first_row[0].dockwidget,
                                     second_row[0].dockwidget,
                                     Qt.Vertical)

        # Tabify
        for column in widgets_layout_clean:
            for row in column:
                for idx in range(len(row) - 1):
                    first, second = row[idx], row[idx+1]
                    self.tabify_plugins(first, second)

                # Raise front widget per row
                row[0].dockwidget.show()
                row[0].dockwidget.raise_()

        # Set dockwidget widths
        width_fractions = layout['width fraction']
        if len(width_fractions) > 1:
            _widgets = [col[0][0].dockwidget for col in widgets_layout]
            self.resizeDocks(_widgets, width_fractions, Qt.Horizontal)

        # Set dockwidget heights
        height_fractions = layout['height fraction']
        for idx, column in enumerate(widgets_layout_clean):
            if len(column) > 1:
                _widgets = [row[0].dockwidget for row in column]
                self.resizeDocks(_widgets, height_fractions[idx], Qt.Vertical)

        # Hide toolbars
        hidden_toolbars = global_hidden_toolbars + layout['hidden toolbars']
        for toolbar in hidden_toolbars:
            if toolbar is not None:
                toolbar.close()

        # Hide widgets
        hidden_widgets = layout['hidden widgets']
        for widget in hidden_widgets:
            if widget is not None:
                widget.dockwidget.close()

        if first_spyder_run:
            self.first_spyder_run = False
        else:
            self.setMinimumWidth(min_width)
            self.setMaximumWidth(max_width)

            if not (self.isMaximized() or self.maximized_flag):
                self.showMaximized()

        self.setUpdatesEnabled(True)
        self.sig_layout_setup_ready.emit(layout)

        return layout