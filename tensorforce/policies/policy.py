# Copyright 2016 reinforce.io. All Rights Reserved.
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
# ==============================================================================

"""
Generic policy class for policy gradients.
"""


class Policy(object):
    def __init__(self):
        pass

    def log_prob(self, dist, action):
        """
        Compute log probability for given policy distribution and actions.
        :param dist:
        :param action:
        :return:
        """
        raise NotImplementedError

    def kl_divergence(self, dist_a, dist_b):
        """
        Get KL divergence between distributions a and b.
        :param dist_a:
        :param dist_b:
        :return:
        """
        raise NotImplementedError

    def entropy(self, dist):
        """
        Get current entropy, mainly used for debugging purposes.
        :param dist:
        :return:
        """
        raise NotImplementedError