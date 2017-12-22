# -*- encoding: utf-8 -*-

"""Each class in the *metadata* module is managed by a facade on present module.
"""

import os
import yaml

from .core import metadata
from .core import settings


class TemplateManager(object):
    """A facade to access the ``metadata.Template```functionalities."""

    def list_templates(self):
        pass

#     def get_template_detail(self,template_name):
#         pass

#     def get_template_info(self,template_name):

#         manager = ParallelManager()
#         info = manager.get_template_info(template_name)

#         return info

#     def get_template_data(self,template_name,cafile_dict):
#         """Pending.

#         Args:
#             template_name (str): The parallel programming pattern name
#                 from which we want a template.
#             cafile_dict (dict): The neccesary data to render the template.

#         Returns:
#              dict: Data of the rendered template.
#         """

#         template = metadata.Template(template_name)
#         cafile = metadata.Cafile(cafile_dict)

#         data = {
#             'name': template.file_name,
#             'ftype': template.file_type,
#             'text': template.render(cafile)
#         }

#         return data

# class ParallelManager(object):

#     def __init__(self):
#         """A facade to access the ``metadata.Parallel`` class functionalities."""
#         pass

#     def get_template_info(self,template_name):
#         """Returns the info of a parallel file.
#         The basic info of a parallel file is the *name* of 
#         the parallel proramming pattern an a *description*
#         of the semantic of the same.

#         Args:
#             template_name (str): The name of the parallel programming
#                 pattern template we request info.

#         Returns:
#             Dict containing the parallel file basic info.
#         """

#         parallel = metadata.Parallel(template_name)
#         info = parallel.get_basic_info()

#         return info

#     def get_parallel_file_data(self,template_name):

#         parallel = metadata.Parallel(template_name)
        
#         data = {
#             'name': parallel.file_name,
#             'ftype': parallel.file_type,
#             'text': parallel.raw
#         }

#         return data