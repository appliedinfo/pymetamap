# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from .MetaMap import MetaMap
from Concept import ConceptMMI
from Concept import ConceptAA
from Concept import ConceptUA
from Concept import Corpus

__all__ = (MetaMap, Corpus)

__authors__ = 'Anthony Rios'
__version__ = '0.1'
__email__ = 'anthonymrios@gmail.com'

if __name__ == '__main__':
	# from pymetamap import MetaMap
	mm = MetaMap.get_instance('/Users/faizaanwani/projects/public_mm/bin/metamap16')
	sents = ['Heart Attack', 'John had a huge heart attack']
	concepts,error = mm.extract_concepts(sents,[1,2])
	for concept in concepts:
		print concept