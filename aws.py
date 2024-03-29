#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 10:07:14 2019

@author: Christo Strydom
"""

# COPYRIGHT:
# 
# Copyright 2018-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# 
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.
# 
#%%
import configparser
config = configparser.ConfigParser()

#config.sections()
config.read('/home/lnr-ai/github_repos/pyAudioAnalysis/config/aws.ini')
config.sections()
config['christo']['Access key ID']

#%%
from __future__ import print_function

import time
import boto3
s3 = boto3.resource('s3',
         aws_access_key_id=ACCESS_ID,
         aws_secret_access_key= ACCESS_KEY)
transcribe = boto3.client('transcribe', region_name='https://sts.eu-west-2.amazonaws.com')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

job_name = "job name"
job_uri = "https://S3 endpoint/test-transcribe/answer2.wav"

transcribe.start_transcription_job(
    TranscriptionJobName=job_name,
    Media={'MediaFileUri': job_uri},
    MediaFormat='wav',
    LanguageCode='en-US'

)

while True:
    status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
    if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
        break
    print("Not ready yet...")
    time.sleep(5)
print(status)
