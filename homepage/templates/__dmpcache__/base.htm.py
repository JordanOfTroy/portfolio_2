# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1558999139.8053846
_enable_loop = True
_template_filename = 'C:/Users/jorda/BrightBridge/tuesdaytraining/mysite/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['content']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html>\r\n    <meta charset="UTF-8">\r\n    <head>\r\n\r\n        <title>DMP</title>\r\n\r\n')
        __M_writer('        <script src="http://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>\r\n\r\n')
        __M_writer('        <script src="/django_mako_plus/dmp-common.min.js"></script>\r\n        ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( django_mako_plus.links(self) ))
        __M_writer('\r\n\r\n        <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.2/css/all.css" integrity="sha384-oS3vJWv+0UjzBfQzYUhtDYW+Pj2yciDJxpsK1OYPAYjqT085Qq/1cq5FLXAZQ7Ay" crossorigin="anonymous">\r\n        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">\r\n        <link href="https://fonts.googleapis.com/css?family=Raleway&display=swap" rel="stylesheet">\r\n    </head>\r\n    <body >\r\n        <header>\r\n            <nav class="navbar navbar-expand-lg navbar-light w-100" id="top_nav">\r\n                <!-- <a class="navbar-brand" href="#">Jordan Smithson</a> -->\r\n                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">\r\n                  <span class="navbar-toggler-icon"></span>\r\n                </button>\r\n              \r\n                <div class="collapse navbar-collapse" id="navbarSupportedContent">\r\n                  <ul class="navbar-nav mr-auto">\r\n                    <li class="nav-item active">\r\n                      <a class="nav-link" href="#home_section">Home <span class="sr-only">(current)</span></a>\r\n                    </li>\r\n                    <li class="nav-item active">\r\n                      <a class="nav-link" href="#about_section">About <span class="sr-only">(current)</span></a>\r\n                    </li>\r\n                    <li class="nav-item active">\r\n                      <a class="nav-link" href="#skills_section">Skills <span class="sr-only">(current)</span></a>\r\n                    </li>\r\n                    <li class="nav-item active">\r\n                      <a class="nav-link" href="#project_section">Projects <span class="sr-only">(current)</span></a>\r\n                    </li>\r\n                    <li class="nav-item active">\r\n                      <a class="nav-link" href="#contact_section">Contact <span class="sr-only">(current)</span></a>\r\n                    </li>\r\n                  </ul>\r\n                </div>\r\n              </nav>\r\n        </header>\r\n\r\n        <main>\r\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n        </main>\r\n\r\n        <footer class="row ">\r\n           \r\n        </footer>\r\n    </body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n              \r\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/jorda/BrightBridge/tuesdaytraining/mysite/homepage/templates/base.htm", "uri": "base.htm", "source_encoding": "utf-8", "line_map": {"18": 0, "26": 2, "27": 10, "28": 13, "29": 14, "30": 14, "35": 53, "41": 51, "47": 51, "53": 47}}
__M_END_METADATA
"""
