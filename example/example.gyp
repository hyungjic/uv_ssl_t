{
  "targets": [{
    "target_name": "uv_ssl_t-example",
    "type": "executable",

    "include_dirs": [
      "src"
    ],

    "variables": {
      "gypkg_deps": [
        "git://github.com/libuv/libuv.git#v1.9.1:uv.gyp:libuv",
        "git://github.com/indutny/uv_link_t:uv_link_t.gyp:uv_link_t",
        "git://github.com/indutny/bud:deps/openssl/openssl.gyp:openssl",
      ],
    },

    "dependencies": [
      "<!@(gypkg deps <(gypkg_deps))",
      "../uv_ssl_t.gyp:uv_ssl_t",
    ],

    "sources": [
      "src/main.c",
      "src/middle.c",
    ],
  }],
}
