# -*- coding: utf-8 -*-
"""_site 를 baseurl(/pa_lab) 아래에 띄운다 — 로컬 미리보기용.

`python -m http.server --directory _site` 로 띄우면 사이트가 / 에 붙어,
테마의 CSS·JS(/pa_lab/assets/...)가 전부 404가 나고 페이지가 스타일 없이 보인다(2026-10-02).
GitHub Pages 와 같은 경로 구조를 만들려고 baseurl 접두사를 떼고 _site 에서 찾는다.

    python .claude/serve_site.py [포트]     # 기본 4012 → http://localhost:4012/pa_lab/
"""
import functools, http.server, io, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(ROOT, '_site')

base = ''
for line in io.open(os.path.join(ROOT, '_config.yml'), encoding='utf-8'):
    m = re.match(r'^baseurl:\s*"?([^"]*?)"?\s*$', line)
    if m:
        base = m.group(1).strip().rstrip('/')
        break


class Handler(http.server.SimpleHTTPRequestHandler):
    def _route(self):
        if base and (self.path == '/' or self.path == base):
            self.send_response(301)
            self.send_header('Location', base + '/')
            self.end_headers()
            return False
        if base and not self.path.startswith(base + '/'):
            self.send_error(404, 'baseurl(%s) 밖의 경로' % base)
            return False
        rest = self.path[len(base):]
        # 끝 슬래시 없는 디렉터리 주소는 여기서 돌려보낸다. 표준 핸들러에 맡기면
        # 접두사를 뗀 경로(/practice/bid/)로 보내 404가 난다.
        bare = rest.split('?', 1)[0].split('#', 1)[0]
        if not bare.endswith('/') and os.path.isdir(os.path.join(SITE, bare.lstrip('/'))):
            self.send_response(301)
            self.send_header('Location', base + bare + '/' + rest[len(bare):])
            self.end_headers()
            return False
        self.path = rest
        return True

    def do_GET(self):
        if self._route():
            super().do_GET()

    def do_HEAD(self):
        if self._route():
            super().do_HEAD()


if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 4012
    handler = functools.partial(Handler, directory=SITE)
    print('http://localhost:%d%s/' % (port, base))
    http.server.ThreadingHTTPServer(('', port), handler).serve_forever()
