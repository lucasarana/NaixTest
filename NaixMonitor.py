__author__ = 'lucas.arana'


# -*- coding: utf-8 -*-
import os
import sys
import signal
import socket
import platform
import threading
import multiprocessing
# import config
from subprocess import Popen, PIPE

from Environment import Environment
# from LeanderCommon.LegaLogger import LegaLogger
# from DataAccess import DAZoe


class NaixMonitor:

    def __init__(self):
        self.algo = 'ee'

    def main(self):
        Environment().reset()
        self.dostuff()

    def dostuff(self):
        print "haciendo listens"

