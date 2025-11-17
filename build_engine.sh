#!/bin/bash

trtexec --onnx=$1 \
        --minShapes=A:1x6x160x160,B:1x6x160x160 \
        --optShapes=A:1x6x160x160,B:1x6x160x160 \
        --maxShapes=A:1x6x160x160,B:1x6x160x160 \
        --fp16 \
        --saveEngine=refine.engine \
	--dumpProfile
#        --optShapes=A:252x6x160x160,B:252x6x160x160 \
#        --maxShapes=A:252x6x160x160,B:252x6x160x160 \
#        --optShapes=A:252x6x160x160,B:252x6x160x160 \
#        --maxShapes=A:252x6x160x160,B:252x6x160x160 \
