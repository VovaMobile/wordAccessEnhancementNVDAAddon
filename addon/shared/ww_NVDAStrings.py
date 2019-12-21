# appModules\winword\ww_NVDAStrings.py
#A part of wordAccessEnhancement add-on
#Copyright (C) 2019 paulber19
#This file is covered by the GNU General Public License.

#A simple module to bypass the addon translation system,
#so it can take advantage from the NVDA translations directly.
#Based on implementation made by Alberto Buffolino
#https://github.com/nvaccess/nvda/issues/4652 """


def NVDAString(s):
	return _(s)
