#!/usr/bin/env python3
# -*- coding: utf-8 -*-

d = {
    'Michael': 95,
    'Bob': 75,
    'Tracy': 85,
    '95':95,
    90:90,
    'stanford':100
}
print('d[\'Michael\'] =', d['Michael'])
print('d[\'Bob\'] =', d['Bob'])
print('d[\'Tracy\'] =', d['Tracy'])
print('d[\'95\'] =',d['95'])
print('d[90] =',d[90])
print('d[stanford] =',d['stanford'])
print('d.get(\'Thomas\', -1) =', d.get('Thomas', -1))
