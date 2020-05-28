.. raw:: mediawiki

   {{Back to|Hacker Guide}}

.. table:: *' C Types*'

   ================== ============= ========== ========== ========= ==========
   name               printf format Win32 size ILP32 size LP64 Size LLP64 Size
   ================== ============= ========== ========== ========= ==========
   signed char        "hhd"         8          8          8         8         
   short              "hd"          16         16         16        16        
   int                "d"           32         32         32        32        
   long               "ld"          32         32         64        32        
   long long          "lld"         64         64         64        64        
   int8_t             PRId8         8          8          8         8         
   int16_t            PRId16        16         16         16        16        
   int32_t            PRId32        32         32         32        32        
   int64_t            PRId64        64         64         64        64        
   intmax_t           "jd"          64         64         64        64        
   unsigned char      "hhu"         8          8          8         8         
   unsigned short     "hu"          16         16         16        16        
   unsigned           "u"           32         32         32        32        
   unsigned long      "lu"          32         32         64        32        
   unsigned long long "llu"         64         64         64        64        
   size_t             "zu"          32         32         64        64        
   uint8_t            PRIu8         8          8          8         8         
   uint16_t           PRIu16        16         16         16        16        
   uint32_t           PRIu32        32         32         32        32        
   uint64_t           PRIu64        64         64         64        64        
   uintmax_t          "ju"          64         64         64        64        
   ================== ============= ========== ========== ========= ==========

`Category:Coding <Category:Coding>`__
