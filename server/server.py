############################################################################
# Copyright(c) Open Law Library. All rights reserved.                      #
# See ThirdPartyNotices.txt in the project root for additional notices.    #
#                                                                          #
# Licensed under the Apache License, Version 2.0 (the "License")           #
# you may not use this file except in compliance with the License.         #
# You may obtain a copy of the License at                                  #
#                                                                          #
#     http: // www.apache.org/licenses/LICENSE-2.0                         #
#                                                                          #
# Unless required by applicable law or agreed to in writing, software      #
# distributed under the License is distributed on an "AS IS" BASIS,        #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. #
# See the License for the specific language governing permissions and      #
# limitations under the License.                                           #
############################################################################
import asyncio
import json
import time
import uuid
from json import JSONDecodeError

from pygls.features import (COMPLETION, TEXT_DOCUMENT_DID_CHANGE,
                            TEXT_DOCUMENT_DID_CLOSE, TEXT_DOCUMENT_DID_OPEN)
from pygls.server import LanguageServer
from pygls.types import (CompletionItem, CompletionList, CompletionParams,
                         ConfigurationItem, ConfigurationParams, Diagnostic,
                         DidChangeTextDocumentParams,
                         DidCloseTextDocumentParams, DidOpenTextDocumentParams,
                         MessageType, Position, Range, Registration,
                         RegistrationParams, Unregistration,
                         UnregistrationParams)

class CodeLanguageServer(LanguageServer):
    CMD_REGISTER_COMPLETIONS = 'registerCompletions'
    CMD_UNREGISTER_COMPLETIONS = 'unregisterCompletions'

    CONFIGURATION_SECTION = 'codeServer'

    def __init__(self):
        super().__init__()


code_server = CodeLanguageServer()

@code_server.feature(COMPLETION, trigger_characters=[','])
def completions(params: CompletionParams):
    """Returns completion items."""
    a = 1
    b = 1
    c = a+b
    return CompletionList(False, [
        CompletionItem('hello',kind=2,data=1),
        CompletionItem('world',kind=2,data=2)
    ])

@code_server.feature(TEXT_DOCUMENT_DID_CHANGE)
def did_change(ls, params: DidChangeTextDocumentParams):
    """Text document did change notification."""
    a = 1
    b = 1
    c = a+b
    # _validate(ls, params)

@code_server.feature(TEXT_DOCUMENT_DID_CLOSE)
def did_close(server: CodeLanguageServer, params: DidCloseTextDocumentParams):
    """Text document did close notification."""
    server.show_message('Text Document Did Close')


@code_server.feature(TEXT_DOCUMENT_DID_OPEN)
async def did_open(ls, params: DidOpenTextDocumentParams):
    """Text document did open notification."""
    ls.show_message('Text Document Did Open')
    # _validate(ls, params)