#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo
import subprocess

# Your test case class goes here


class TestEcho(unittest.TestCase):
    word = "HeLlO"
    truth_table = {
        "-u": "HELLO",
        "--upper": "HELLO",
        "-l": "hello",
        "--lower": "hello",
        "-t": "Hello",
        "--title": "Hello"
    }

    def setUp(self):
        self.parser = echo.create_parser()

    def test_help(self):
        """ Running the program without arguments should show usage. """

        # Run the command `python ./echo.py -h` in a separate process, then
        # collect it's output.
        process = subprocess.Popen(
            ["python", "echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()
        print (usage)
        print (stdout)
        self.assertEquals(stdout, usage)

        # Write a unit test that asserts that upper get stored inside of the
        # namespace returned from parser.parse_args when either "-u" or
        # "--upper" arguments are passed.

    def test_all_options(self):
        for k, v in self.truth_table.items():
            result = echo.main([k, self.word])
            self.assertEquals(result, v)


if __name__ == '__main__':
    unittest.main()
