__author__ = 'lucas.arana'
# -*- coding: utf-8 -*-

from Environment import Environment

class NaixMonitor:
    """
    Class for Monitor listening (once per sec)
    """
    def __init__(self):
        """
        Still No Use
        """
        self.algo = 'ee'

    def main(self):
        """
        Main (Reset does not do anything yet)
        """
        Environment().reset()
        self.dostuff()

    def dostuff(self):
        """
        Just checking if monitor is on
        """
        print "Doing Listens"

