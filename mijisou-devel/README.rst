秘迹搜索开源说明
=============
秘迹搜索是基于开源项目Searx进行二次开发的，因为Searx采用的开源协议是AGPL-3.0，秘迹搜索(https://mijisou.com)严格遵守这一开源协议，将我们所有的改动同步开源出来。欢迎对网络隐私防护感兴趣的朋友们一起开发和维护秘迹搜索。

秘迹®️是熵加网络科技（北京）有限公司所持有的注册商标，任何组织或个人在使用代码前请去除任何和秘迹相关字段,去除秘迹搜索的UI设计，否则熵加网络科技（北京）有限公司保留追究法律责任的权利。 


环境搭建
~~~~~~
- 安装python3环境，使用python3运行秘迹搜索的代码。pip3 install -r requirements.txt
- 在正式运行代码前，请正确设置配置文件settings_et_dev.yml。秘迹搜索使用了redis 作为缓存，使用sentry收集异常信息。
- 设置完成后，可在测试环境执行 env FLASK_APP=searx.webapp FLASK_ENV=development FLASK_DEBUG=1 SEARX_SETTINGS_PATH=settings_et_dev.yml python -m flask run

Entropage theme
~~~~~~~~~~~~~~~
- cd searx/static/themes/entropage
- npm i
- npm start
less: themes/entropage/less

js: themes/entropage/js/searx_src

秘迹搜索反馈渠道和联系方式
~~~~~~~~~~~~~~~~~~~~~
微信: mijixiaoer

邮件: contact@entropage.com



searx
=====

A privacy-respecting, hackable `metasearch
engine <https://en.wikipedia.org/wiki/Metasearch_engine>`__.

Pronunciation: səːks

List of `running
instances <https://github.com/asciimoo/searx/wiki/Searx-instances>`__.

See the `documentation <https://asciimoo.github.io/searx>`__ and the `wiki <https://github.com/asciimoo/searx/wiki>`__ for more information.

|OpenCollective searx backers|
|OpenCollective searx sponsors|

Installation
~~~~~~~~~~~~

-  clone source:
   ``git clone https://github.com/asciimoo/searx.git && cd searx``
-  install dependencies: ``./manage.sh update_packages``
-  edit your
   `settings.yml <https://github.com/asciimoo/searx/blob/master/searx/settings.yml>`__
   (set your ``secret_key``!)
-  run ``python searx/webapp.py`` to start the application

For all the details, follow this `step by step
installation <https://github.com/asciimoo/searx/wiki/Installation>`__.

Bugs
~~~~

Bugs or suggestions? Visit the `issue
tracker <https://github.com/asciimoo/searx/issues>`__.

`License <https://github.com/asciimoo/searx/blob/master/LICENSE>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

More about searx
~~~~~~~~~~~~~~~~

-  `openhub <https://www.openhub.net/p/searx/>`__
-  `twitter <https://twitter.com/Searx_engine>`__
-  IRC: #searx @ freenode


.. |OpenCollective searx backers| image:: https://opencollective.com/searx/backers/badge.svg
   :target: https://opencollective.com/searx#backer


.. |OpenCollective searx sponsors| image:: https://opencollective.com/searx/sponsors/badge.svg
   :target: https://opencollective.com/searx#sponsor
