#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2022 Stéphane Caron
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

"""
Git utility functions to clone model repositories.
"""

from dataclasses import dataclass


@dataclass
class Repository:

    """
    Remote git repository.

    Attributes:
        cache_path: Path to clone the repository to in the local cache.
        commit: Commit ID or tag to checkout after cloning.
        url: URL to the remote git repository.
    """

    cache_path: str
    commit: str
    url: str


REPOSITORIES = {
    "anymal_b_simple_description": Repository(
        url="https://github.com/ANYbotics/anymal_b_simple_description.git",
        commit="988b5df22b84761bdf08111b1c2ccc883793f456",
        cache_path="ANYbotics/anymal_b_simple_description",
    ),
    "anymal_c_simple_description": Repository(
        url="https://github.com/ANYbotics/anymal_c_simple_description.git",
        commit="f160b8f7fed840c47a6febe8e2bc78b32bf43a68",
        cache_path="ANYbotics/anymal_c_simple_description",
    ),
    "baxter_common": Repository(
        url="https://github.com/RethinkRobotics/baxter_common.git",
        commit="v1.2.0",
        cache_path="RethinkRobotics/baxter_common",
    ),
    "bullet3": Repository(
        url="https://github.com/bulletphysics/bullet3.git",
        commit="3.24",
        cache_path="bulletphysics/bullet3",
    ),
    "cassie_description": Repository(
        url="https://github.com/UMich-BipedLab/cassie_description.git",
        commit="96323f3d0cc2cb7101cb92d7fcf4650abdcb2e81",
        cache_path="UMich-BipedLab/cassie_description",
    ),
    "cassie_mj_description": Repository(
        url="https://github.com/rohanpsingh/cassie_mj_description.git",
        commit="fcc3775453e4da6797cd4eacd3d8321d9906755a",
        cache_path="rohanpsingh/cassie_mj_description",
    ),
    "drake": Repository(
        url="https://github.com/RobotLocomotion/drake.git",
        commit="v1.7.0",
        cache_path="RobotLocomotion/drake",
    ),
    "eDO_description": Repository(
        url="https://github.com/Comau/eDO_description.git",
        commit="17b3f92f834746106d6a4befaab8eeab3ac248e6",
        cache_path="Comau/eDO_description",
    ),
    "example-robot-data": Repository(
        url="https://github.com/Gepetto/example-robot-data.git",
        commit="v4.0.1",
        cache_path="Gepetto/example-robot-data",
    ),
    "gym-pybullet-drones": Repository(
        url="https://github.com/utiasDSL/gym-pybullet-drones.git",
        commit="v1.0.0",
        cache_path="utiasDSL/gym-pybullet-drones",
    ),
    "icub-models": Repository(
        url="https://github.com/robotology/icub-models.git",
        commit="v1.25.0",
        cache_path="robotology/icub-models",
    ),
    "jvrc_description": Repository(
        url="https://github.com/stephane-caron/jvrc_description.git",
        commit="v1.1.0",
        cache_path="stephane-caron/jvrc_description",
    ),
    "jvrc_mj_description": Repository(
        url="https://github.com/isri-aist/jvrc_mj_description.git",
        commit="0f0ce7daefdd66c54e0909a6bf2c22154844f5f3",
        cache_path="isri-aist/jvrc_mj_description",
    ),
    "mini_cheetah_urdf": Repository(
        url="https://github.com/Derek-TH-Wang/mini_cheetah_urdf.git",
        commit="1988bceb26e81f28594a16e7d5e6abe5cbb27ace",
        cache_path="Derek-TH-Wang/mini_cheetah_urdf",
    ),
    "mujoco_menagerie": Repository(
        url="https://github.com/deepmind/mujoco_menagerie.git",
        commit="2665e9bc0f476e5f505ff929d758ed36f8618fa8",
        cache_path="deepmind/mujoco_menagerie",
    ),
    "reachy_description": Repository(
        url="https://github.com/aubrune/reachy_description.git",
        commit="release-1.0.0",
        cache_path="aubrune/reachy_description",
    ),
    "robot-assets": Repository(
        url="https://github.com/ankurhanda/robot-assets.git",
        commit="12f1a3c89c9975194551afaed0dfae1e09fdb27c",
        cache_path="ankurhanda/robot-assets",
    ),
    "robotiq_arg85_description": Repository(
        url="https://github.com/a-price/robotiq_arg85_description.git",
        commit="a65190bdbb0666609fe7e8c3bb17341e09e81625",
        cache_path="a-price/robotiq_arg85_description",
    ),
    "romeo_robot": Repository(
        url="https://github.com/ros-aldebaran/romeo_robot.git",
        commit="0.1.5",
        cache_path="ros-aldebaran/romeo_robot",
    ),
    "simple_humanoid_description": Repository(
        url="https://github.com/laas/simple_humanoid_description.git",
        commit="v1.1.0",
        cache_path="laas/simple_humanoid_description",
    ),
    "talos-data": Repository(
        url="https://github.com/stack-of-tasks/talos-data.git",
        commit="v2.0.0",
        cache_path="stack-of-tasks/talos-data",
    ),
    "unitree_mujoco": Repository(
        url="https://github.com/unitreerobotics/unitree_mujoco.git",
        commit="f3300ff1bf0ab9efbea0162717353480d9b05d73",
        cache_path="unitreerobotics/unitree_mujoco",
    ),
    "unitree_ros": Repository(
        url="https://github.com/unitreerobotics/unitree_ros.git",
        commit="92a36c7cf2fe7781adedce30cd6a6ab1456ef56c",
        cache_path="unitreerobotics/unitree_ros",
    ),
    "upkie_description": Repository(
        url="https://github.com/tasts-robots/upkie_description.git",
        commit="v1.1.0",
        cache_path="tasts-robots/upkie_description",
    ),
}
