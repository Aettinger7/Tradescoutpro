2026-01-20T18:57:25.697780205Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/app/wsgiapp.py", line 57, in load
2026-01-20T18:57:25.697782725Z     return self.load_wsgiapp()
2026-01-20T18:57:25.697785245Z            ~~~~~~~~~~~~~~~~~^^
2026-01-20T18:57:25.697788085Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/app/wsgiapp.py", line 47, in load_wsgiapp
2026-01-20T18:57:25.697790665Z     return util.import_app(self.app_uri)
2026-01-20T18:57:25.697793315Z            ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^
2026-01-20T18:57:25.697795905Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/util.py", line 417, in import_app
2026-01-20T18:57:25.697798785Z     raise AppImportError("Failed to find attribute %r in %r." % (name, module))
2026-01-20T18:57:25.697807066Z gunicorn.errors.AppImportError: Failed to find attribute 'app' in 'main'.
2026-01-20T18:57:32.029070777Z ==> Exited with status 1
2026-01-20T18:57:32.102611974Z ==> Common ways to troubleshoot your deploy: https://render.com/docs/troubleshooting-deploys
2026-01-20T18:57:36.028382913Z ==> Running 'gunicorn main:app'
2026-01-20T18:57:37.130834137Z Traceback (most recent call last):
2026-01-20T18:57:37.13097084Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/util.py", line 413, in import_app
2026-01-20T18:57:37.130977221Z     app = getattr(mod, name)
2026-01-20T18:57:37.130980341Z AttributeError: module 'main' has no attribute 'app'
2026-01-20T18:57:37.131014262Z 
2026-01-20T18:57:37.131021322Z During handling of the above exception, another exception occurred:
2026-01-20T18:57:37.131023432Z 
2026-01-20T18:57:37.131025542Z Traceback (most recent call last):
2026-01-20T18:57:37.132561399Z   File "/opt/render/project/src/.venv/bin/gunicorn", line 8, in <module>
2026-01-20T18:57:37.132572669Z     sys.exit(run())
2026-01-20T18:57:37.132575759Z              ~~~^^
2026-01-20T18:57:37.132578639Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/app/wsgiapp.py", line 66, in run
2026-01-20T18:57:37.132580899Z     WSGIApplication("%(prog)s [OPTIONS] [APP_MODULE]", prog=prog).run()
2026-01-20T18:57:37.132582959Z     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^
2026-01-20T18:57:37.132585089Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/app/base.py", line 235, in run
2026-01-20T18:57:37.132587179Z     super().run()
2026-01-20T18:57:37.13258929Z     ~~~~~~~~~~~^^
2026-01-20T18:57:37.132591499Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/app/base.py", line 71, in run
2026-01-20T18:57:37.132593519Z     Arbiter(self).run()
2026-01-20T18:57:37.13259578Z     ~~~~~~~^^^^^^
2026-01-20T18:57:37.13259795Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/arbiter.py", line 57, in __init__
2026-01-20T18:57:37.13260008Z     self.setup(app)
2026-01-20T18:57:37.13260217Z     ~~~~~~~~~~^^^^^
2026-01-20T18:57:37.13260434Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/arbiter.py", line 117, in setup
2026-01-20T18:57:37.1326064Z     self.app.wsgi()
2026-01-20T18:57:37.1326085Z     ~~~~~~~~~~~~~^^
2026-01-20T18:57:37.13261066Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/app/base.py", line 66, in wsgi
2026-01-20T18:57:37.13261356Z     self.callable = self.load()
2026-01-20T18:57:37.13261562Z                     ~~~~~~~~~^^
2026-01-20T18:57:37.13261775Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/app/wsgiapp.py", line 57, in load
2026-01-20T18:57:37.13261982Z     return self.load_wsgiapp()
2026-01-20T18:57:37.13262187Z            ~~~~~~~~~~~~~~~~~^^
2026-01-20T18:57:37.13262449Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/app/wsgiapp.py", line 47, in load_wsgiapp
2026-01-20T18:57:37.13262739Z     return util.import_app(self.app_uri)
2026-01-20T18:57:37.13262956Z            ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^
2026-01-20T18:57:37.132631651Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/util.py", line 417, in import_app
2026-01-20T18:57:37.132633831Z     raise AppImportError("Failed to find attribute %r in %r." % (name, module))
2026-01-20T18:57:37.132635911Z gunicorn.errors.AppImportError: Failed to find attribute 'app' in 'main'.
