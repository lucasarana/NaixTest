__author__ = 'lucas.arana'
# -*- coding: utf-8 -*-

from Environment import Environment

class NaixMonitor:

    def __init__(self):
        self.algo = 'ee'

    def main(self):
        Environment().reset()
        self.dostuff()

    def dostuff(self):
        print "haciendo listens"

