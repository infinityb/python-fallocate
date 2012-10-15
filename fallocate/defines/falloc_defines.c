#include <stdlib.h>
#include <errno.h>
#include <fcntl.h>
#include <linux/falloc.h>
#include "../ext/cconst/cdefine.h"

const struct constdefs falloc_defs = {
    .name = "falloc_defs",
    .members = (struct constdef[]) {
#ifdef FALLOC_FL_KEEP_SIZE
    	{
    		.name = "FALLOC_FL_KEEP_SIZE",
    		.value = FALLOC_FL_KEEP_SIZE
    	},
#endif /* FALLOC_FL_KEEP_SIZE */
#ifdef FALLOC_FL_PUNCH_HOLE
    	{
    		.name = "FALLOC_FL_PUNCH_HOLE",
    		.value = FALLOC_FL_PUNCH_HOLE
    	},
#endif /* FALLOC_FL_PUNCH_HOLE */
    	{
    		.name = NULL,
    		.value = 0
    	}
    }
};

const struct constdefs errcode_defs = {
    .name = "errcode_defs",
    .members = (struct constdef[]) {
        {
            .name = "EBADF",
            .value = EBADF
        },
        {
            .name = "EFBIG",
            .value = EFBIG
        },
        {
            .name = "EINTR",
            .value = EINTR
        },
        {
            .name = "EINVAL",
            .value = EINVAL
        },
        {
            .name = "EIO",
            .value = EIO
        },
        {
            .name = "ENODEV",
            .value = ENODEV
        },
        {
            .name = "ENOSPC",
            .value = ENOSPC
        },
        {
            .name = "ENOSYS",
            .value = ENOSYS
        },
        {
            .name = "EOPNOTSUPP",
            .value = EOPNOTSUPP
        },
        {
            .name = NULL,
            .value = 0
        }
    }
};