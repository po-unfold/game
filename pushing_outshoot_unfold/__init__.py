# This file must exist, empty or not
# -*- coding: utf-8 -*-
# KEEP THAT! ^^^^^

# This is for the website:
class Term:
	def __getattribute__(self, name):
		class _r:
			def __repr__(self):
				return ""
			def __call__(self, i, *args, **kwargs):
				return i
		return _r()