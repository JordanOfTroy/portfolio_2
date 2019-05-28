# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1559005310.4621916
_enable_loop = True
_template_filename = 'C:/Users/jorda/BrightBridge/tuesdaytraining/mysite/homepage/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        csrf_input = context.get('csrf_input', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        def content():
            return render_content(context)
        csrf_input = context.get('csrf_input', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <!-------------------------- HOME SECTION ---------------------------------->\r\n    <div class="section hero " id="home_section">\r\n        <div class="row text-center h-100 d-flex align-items-center">\r\n            <div class="col-9">\r\n                <div class="row d-flex justify-content-center">\r\n                    <div class="col-sm-12 col-lg-5" id="landingText">\r\n                        <h1>Jordan Smithson</h1>\r\n                        <p>Full Stack Web Developer || Let\'s build something epic.</p>\r\n                        <p><a href="https://www.linkedin.com/in/jordan-smithson/" target="_blank" style="color: var(--wht);"><i class="fab fa-linkedin"></i> LinkedIn</a> || <a href="https://github.com/JordanOfTroy" target="_blank" style="color: var(--wht);"><i class="fab fa-github-square"></i> GitHub</a></p>\r\n                    </div>\r\n                </div>\r\n            </div>\r\n        </div>\r\n    </div>\r\n\r\n\r\n    <!-------------------------- ABOUT SECTION ---------------------------------->\r\n    <div class="section " id="about_section">\r\n        <div class="row d-flex justify-content-around p-5">\r\n            <h2>About</h2>\r\n            <a href="#top_nav">back to top <i class="fas fa-arrow-up"></i></a>\r\n        </div>\r\n        <div class="row">\r\n            <div class="col-6 d-flex justify-content-center align-items-center">\r\n                <img class="img-fluid w-50 my-3 headshot" src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
        __M_writer('homepage/media/headshot.jpg" alt="head shot">\r\n           </div>\r\n           <div class="col-6">\r\n                <div class="row mr-5">\r\n                    <div class="card m-5 quote">\r\n                        <div class="card-body">\r\n                            <blockquote class="blockquote m-2">\r\n                            <p>It is important to draw wisdom from different places. If you take it from only one source it becomes rigid and stale.</p>\r\n                            <footer class="blockquote-footer">Uncle Iroh, <cite title="Source Title">Avatar: The Last Airbender</cite></footer>\r\n                            </blockquote>\r\n                        </div>\r\n                    </div>\r\n                </div>\r\n                <div class="row">\r\n                    more text\r\n                </div>\r\n           </div>\r\n       </div>\r\n    </div>\r\n\r\n\r\n    <!-------------------------- SKILLS SECTION ---------------------------------->\r\n    <div class="section" id="skills_section">\r\n            <div class="row d-flex justify-content-around">\r\n                    <h2>Skills</h2>\r\n                    <a href="#top_nav">back to top <i class="fas fa-arrow-up"></i></a>\r\n                </div>\r\n        <div class="row">\r\n            <div class="col-12">\r\n                <h1>Skills</h1>\r\n            </div>\r\n        </div>\r\n    </div>\r\n\r\n\r\n    <!-------------------------- PROJECTS SECTION ---------------------------------->\r\n    <div class="section" id="project_section">\r\n            <div class="row d-flex justify-content-around">\r\n                    <h2>Projects</h2>\r\n                    <a href="#top_nav">back to top <i class="fas fa-arrow-up"></i></a>\r\n                </div>\r\n        <div class="row">\r\n            <div class="col-12">\r\n                <h1>Projects</h1>\r\n            </div>\r\n        </div>\r\n    </div>\r\n\r\n\r\n    <!-------------------------- CONTACT SECTION ---------------------------------->\r\n    <div class="section " id="contact_section">\r\n        <div class="row contact_header p-5">\r\n            <div class="col-12 d-flex justify-content-around">\r\n                <h2>Contact</h2>\r\n                <a href="#top_nav">back to top <i class="fas fa-arrow-up"></i></a>\r\n            </div>\r\n        </div>\r\n        <div class="row d-flex justify-content-center ">\r\n            <div class="col-6 p-5 mt-5 contact_form">\r\n                <form class="form-group" method="POST"> ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(csrf_input))
        __M_writer('\r\n                    <div class="row p-2">\r\n                        <div class="col-6 p-2">\r\n                            <div class="input-group mb-3">\r\n                                <input name="name" type="text" class="form-control custom_input" placeholder="Your Name" aria-label="Recipient\'s username" aria-describedby="basic-addon2" required>\r\n                                <div class="input-group-append">\r\n                                    <span class="input-group-text" id="basic-addon2"><i class="fas fa-user-alt"></i></span>\r\n                                </div>\r\n                            </div>\r\n                        </div>\r\n                        <div class="col-6 p-2">\r\n                            <div class="input-group mb-3">\r\n                                <input name="email" type="text" class="form-control custom_input" placeholder="Your Email" aria-label="Recipient\'s username" aria-describedby="basic-addon2" required>\r\n                                <div class="input-group-append">\r\n                                    <span class="input-group-text" id="basic-addon2"><i class="fas fa-at"></i></span>\r\n                                </div>\r\n                            </div>\r\n                        </div>\r\n                    </div>\r\n                    <div class="row">\r\n                        <div class="col-12">\r\n                            <div class="input-group mb-4">\r\n                                <textarea name="message" class="form-control custom_input" aria-label="With textarea" placeholder="Your Message" required></textarea>\r\n                                <div class="input-group-append">\r\n                                    <span class="input-group-text"><i class="far fa-keyboard fa-3x"></i></span>\r\n                                </div>\r\n                            </div>\r\n                        </div>\r\n                    </div>\r\n                    <div class="row pb-1">\r\n                        <div class="col-12">\r\n                            <button class="btn btn-success send_email p-3">Send Message</button>\r\n                        </div>\r\n                    </div>\r\n                </form>\r\n            </div>\r\n        </div>\r\n    </div>\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/jorda/BrightBridge/tuesdaytraining/mysite/homepage/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "39": 1, "44": 127, "50": 3, "59": 3, "60": 28, "61": 28, "62": 87, "63": 87, "69": 63}}
__M_END_METADATA
"""
