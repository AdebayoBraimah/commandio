# -*- coding: utf-8 -*-
#
# Adebayo Braimah
#
# Copyright 2021
#
# GNU GENERAL PUBLIC LICENSE v3
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The :mod: ``commandio`` package contains modules for reading/writing files,
logging, and running commands on the command line.
"""
import os

name: str = "commandio"


# Define constants
_MISCDIR: str = os.path.abspath("misc")
_LICENSE: str = "GNU GENERAL PUBLIC LICENSE v3"

_version_file: str = os.path.abspath(os.path.join(_MISCDIR, "version.txt"))

with open(_version_file, "r") as f:
    file_contents: str = f.read()
    _version: str = file_contents.strip("\n")


__author__ = "Adebayo Braimah"
__credits__ = ["Adebayo Braimah"]
__license__ = _LICENSE
__version__ = _version
__maintainer__ = "Adebayo Braimah"
__email__ = "adebayo.braimah@gmail.com"
__status__ = "Development"
