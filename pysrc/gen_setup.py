#!/usr/bin/env python
# -*- python -*-
#BEGIN_LEGAL
#
#Copyright (c) 2019 Intel Corporation
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#  
#END_LEGAL

import argparse
import os
import sys

def die(s):
    sys.stdout.write("ERROR: {0}\n".format(s))
    sys.exit(1)
def msgb(b,s=''):
    sys.stdout.write("[{0}] {1}\n".format(b,s))
def msge(b,s=''):
    sys.stderr.write("[{0}] {1}\n".format(b,s))
    
def check_exist(fn):
    if not os.path.exists(fn):
        die("Could not find {}".format(fn))
    return fn



def create(help_string=''):
    parser = argparse.ArgumentParser(description=help_string)
    parser.add_argument('prefix', 
                        help='Path to obj/dgen directory')
    return parser
    
def parse(parser):
    def _check_jn(x,y):
        return check_exist(os.path.join(x,y))

    args = parser.parse_args()

    args.state_bits_filename    = _check_jn(args.prefix, 'all-state.txt')
    args.cpuid_filename         = _check_jn(args.prefix, 'all-cpuid.txt')
    args.instructions_filename  = _check_jn(args.prefix, 'all-dec-instructions.txt')
    args.chip_filename          = _check_jn(args.prefix, 'all-chip-models.txt')
    args.widths_filename        = _check_jn(args.prefix, 'all-widths.txt')
    args.element_types_filename = _check_jn(args.prefix, 'all-element-types.txt')
    return args

def setup(help_string=''):
    parser = create(help_string)
    return parse(parser)

    
