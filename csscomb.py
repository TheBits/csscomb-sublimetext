# -*- coding: utf-8 -*-
import subprocess

import sublime
import sublime_plugin

__all__ = [
    'CsscombCommand',
]

PHP_PATH = r"d:\\php\\php-win.exe"
CSSCOMB_PATH = r"d:\\Projects\\csscomb\\plugins\\2.08\\CSScomb_2.08_for_WebStorm-IntelliJIDEA-PyCharm\\csscomb.php"

class CsscombCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        filename = self.view.file_name()
        if filename is None:
            return
        cmd = r'{0} {1} {2}'.format(PHP_PATH, CSSCOMB_PATH, filename)
        # cmd = cmd.replace()
        print cmd
        subprocess.call(cmd, shell=False)
        # subprocess.call(filename, shell=True)
