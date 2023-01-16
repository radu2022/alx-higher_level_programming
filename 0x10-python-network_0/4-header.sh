#!/bin/bash
#pass a variable in the header of the request
curl -sH "X-School-User-Id: 98" "$1"
