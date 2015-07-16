__author__ = 'lucas.arana'
# -*- coding: utf-8 -*-

from Environment import Environment

class NaixMonitor:
    """Monitor listening every second"""
    def __init__(self):
        """If we need something initialized"""
        self.algo = 'ee'

    def main(self):
        """Main (Reset does not do anything yet)"""
        Environment().reset()
        self.dostuff()

    def dostuff(self):
        print "haciendo listens"

