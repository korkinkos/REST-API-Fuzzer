*********************
Fuzzer
*********************

Templates
=====================

------------------
Functions:
------------------

~~~~~~~~~~~~~~~~~~
fuzzer:
~~~~~~~~~~~~~~~~~~
.. code-block:: python

   def convert_cookies_format(cookies):
      """Convert cookies from dictionary to array.
         Argument:
            cookies(dict) - dictionary that contains cookies from session
         Return:
            new_cookies(array) - array of strings of format 'key=value'"""
   def convert_types(formatted_dict):
      """TODO"""
   def authorize():
      """Authorize on server* and return session.
         Return:
            session(Session) - object of current session"""
   def parse_params(params, fuzz=''):
      """Parse queryParameters and return result
         Arguments:
            params(array) - array of queryParameters
            fuzz(dict/string) - contain queryParameter or empty string
         Return:
            result(string) - string of format 'key=value&key=value&...'"""
   def fuzz_first_step(page):
      """Fuzz server and look for undeclared pages.
         """

~~~~~~~~~~~~~~~~~~
py_parser:
~~~~~~~~~~~~~~~~~~
.. code-block:: python

   def parse(parsed_page, page, data):
      """Parse data from JSON to usable dictionary.
         Use recursion to parse all pages.
         Arguments:
            parsed_page(dict) - dictionary that will contains usable data
            page(dict) - dictionary that contains usable data
            data(dict) - dictionary that contains data from JSON"""
   def fetch_parsed_data():
      """Fetch data from json, parse it and return parsed data.
         Use function parse to parse data from JSON to usable format.
         Return:
            parsed_data(dict) - dictionary that contains usable data"""

~~~~~~~~~~~~~~~~~~
consts:
~~~~~~~~~~~~~~~~~~
.. code-block:: python

   domain = ''
   """domain(string) - const string that contains domain of server"""
   req_types = []
   """req_types(array) - const array that contains data for fuzzing"""
   types = {}
   """types(dict) - const dictionary that contains regexes for fuzzing"""

~~~~~~~~~~~~~~~~~~
run:
~~~~~~~~~~~~~~~~~~
.. code-block:: python

   def get_access_token(code, request):
      """func for getting token"""
   def selenium_test(request):
      """func for tests"""
   def give_me_link(request):
      """func for linkedin's link"""











