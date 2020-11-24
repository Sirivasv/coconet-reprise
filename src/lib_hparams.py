# Copyright 2020
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

def get_hparams_object(hparams):
  hyperparams_obj = HyperparameterDefinitions(hparams)
  return hyperparams_obj

class HyperparameterDefinitions(object):

  def __init__(self, hparams):
    self.shortest_duration = hparams["shortest_duration"]
    self.min_pitch = hparams["min_pitch"]
    self.max_pitch = hparams["max_pitch"]
    self.separate_instruments = hparams["separate_instruments"]
    self.num_instruments = hparams["num_instruments"]
    self.quantization_level = hparams["quantization_level"]
