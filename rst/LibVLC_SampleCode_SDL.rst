.. raw:: mediawiki

   {{Lowercase}}

.. raw:: mediawiki

   {{Example code|for=libVLC|l=WTFPL}}

Rendering into a custom surface
-------------------------------

This sample code will render a video into an SDL surface.

**It requires LibVLC 1.1.1 or later.** Below is a version with `SDL 2.0 <#SDL_2.0>`__ and one with `older LibVLC API <#Older_API>`__.

.. code:: c

   /* libSDL and libVLC sample code
    * Copyright © 2008 Sam Hocevar <sam@zoy.org>
    * license: [http://en.wikipedia.org/wiki/WTFPL WTFPL] */

   #include <stdio.h>
   #include <stdint.h>
   #include <math.h>
   #include <stdlib.h>
   #include <assert.h>

   #include <SDL/SDL.h>
   #include <SDL/SDL_mutex.h>

   #include <vlc/vlc.h>

   #define WIDTH 640
   #define HEIGHT 480

   #define VIDEOWIDTH 320
   #define VIDEOHEIGHT 240

   struct ctx
   {
       SDL_Surface *surf;
       SDL_mutex *mutex;
   };

   static void *lock(void *data, void **p_pixels)
   {
       struct ctx *ctx = data;

       SDL_LockMutex(ctx->mutex);
       SDL_LockSurface(ctx->surf);
       *p_pixels = ctx->surf->pixels;
       return NULL; /* picture identifier, not needed here */
   }

   static void unlock(void *data, void *id, void *const *p_pixels)
   {
       struct ctx *ctx = data;

       /* VLC just rendered the video, but we can also render stuff */
       uint16_t *pixels = *p_pixels;
       int x, y;

       for(y = 10; y < 40; y++)
           for(x = 10; x < 40; x++)
               if(x < 13 || y < 13 || x > 36 || y > 36)
                   pixels[y * VIDEOWIDTH + x] = 0xffff;
               else
                   pixels[y * VIDEOWIDTH + x] = 0x0;

       SDL_UnlockSurface(ctx->surf);
       SDL_UnlockMutex(ctx->mutex);

       assert(id == NULL); /* picture identifier, not needed here */
   }

   static void display(void *data, void *id)
   {
       /* VLC wants to display the video */
       (void) data;
       assert(id == NULL);
   }

   int main(int argc, char *argv[])
   {
       libvlc_instance_t *libvlc;
       libvlc_media_t *m;
       libvlc_media_player_t *mp;
       char const *vlc_argv[] =
       {
           "--no-audio", /* skip any audio track */
           "--no-xlib", /* tell VLC to not use Xlib */
       };
       int vlc_argc = sizeof(vlc_argv) / sizeof(*vlc_argv);

       SDL_Surface *screen, *empty;
       SDL_Event event;
       SDL_Rect rect;
       int done = 0, action = 0, pause = 0, n = 0;

       struct ctx ctx;

       if(argc < 2)
       {
           printf("Usage: %s <filename>\n", argv[0]);
           return EXIT_FAILURE;
       }

       /*
        *  Initialise libSDL
        */
       if(SDL_Init(SDL_INIT_VIDEO | SDL_INIT_EVENTTHREAD) == -1)
       {
           printf("cannot initialize SDL\n");
           return EXIT_FAILURE;
       }

       empty = SDL_CreateRGBSurface(SDL_SWSURFACE, VIDEOWIDTH, VIDEOHEIGHT,
                                    32, 0, 0, 0, 0);
       ctx.surf = SDL_CreateRGBSurface(SDL_SWSURFACE, VIDEOWIDTH, VIDEOHEIGHT,
                                       16, 0x001f, 0x07e0, 0xf800, 0);

       ctx.mutex = SDL_CreateMutex();

       int options = SDL_ANYFORMAT | SDL_HWSURFACE | SDL_DOUBLEBUF;

       screen = SDL_SetVideoMode(WIDTH, HEIGHT, 0, options);
       if(!screen)
       {
           printf("cannot set video mode\n");
           return EXIT_FAILURE;
       }

       /*
        *  Initialise libVLC
        */
       libvlc = libvlc_new(vlc_argc, vlc_argv);
       m = libvlc_media_new_path(libvlc, argv[1]);
       mp = libvlc_media_player_new_from_media(m);
       libvlc_media_release(m);

       libvlc_video_set_callbacks(mp, lock, unlock, display, &ctx);
       libvlc_video_set_format(mp, "RV16", VIDEOWIDTH, VIDEOHEIGHT, VIDEOWIDTH*2);
       libvlc_media_player_play(mp);

       /*
        *  Main loop
        */
       rect.w = 0;
       rect.h = 0;

       while(!done)
       { 
           action = 0;

           /* Keys: enter (fullscreen), space (pause), escape (quit) */
           while( SDL_PollEvent( &event ) ) 
           { 
               switch(event.type)
               {
               case SDL_QUIT:
                   done = 1;
                   break;
               case SDL_KEYDOWN:
                   action = event.key.keysym.sym;
                   break;
               }
           }

           switch(action)
           {
           case SDLK_ESCAPE:
               done = 1;
               break;
           case SDLK_RETURN:
               options ^= SDL_FULLSCREEN;
               screen = SDL_SetVideoMode(WIDTH, HEIGHT, 0, options);
               break;
           case ' ':
               pause = !pause;
               break;
           }

           rect.x = (int)((1. + .5 * sin(0.03 * n)) * (WIDTH - VIDEOWIDTH) / 2);
           rect.y = (int)((1. + .5 * cos(0.03 * n)) * (HEIGHT - VIDEOHEIGHT) / 2);

           if(!pause)
               n++;

           /* Blitting the surface does not prevent it from being locked and
            * written to by another thread, so we use this additional mutex. */
           SDL_LockMutex(ctx.mutex);
           SDL_BlitSurface(ctx.surf, NULL, screen, &rect);
           SDL_UnlockMutex(ctx.mutex);

           SDL_Flip(screen);
           SDL_Delay(10);

           SDL_BlitSurface(empty, NULL, screen, &rect);
       }

       /*
        * Stop stream and clean up libVLC
        */
       libvlc_media_player_stop(mp);
       libvlc_media_player_release(mp);
       libvlc_release(libvlc);

       /*
        * Close window and clean up libSDL
        */
       SDL_DestroyMutex(ctx.mutex);
       SDL_FreeSurface(ctx.surf);
       SDL_FreeSurface(empty);

       SDL_Quit();

       return 0;
   }

SDL 2.0
~~~~~~~

This version works with `LibVLC <LibVLC>`__ 1.1.1 or later and SDL 2.0.

.. code:: c

   // libSDL and libVLC sample code.
   // License: [http://en.wikipedia.org/wiki/WTFPL WTFPL]

   #include <stdio.h>
   #include <stdint.h>
   #include <math.h>
   #include <stdlib.h>
   #include <assert.h>

   #include "SDL/SDL.h"
   #include "SDL/SDL_mutex.h"

   #include "vlc/vlc.h"

   #define WIDTH 640
   #define HEIGHT 480

   #define VIDEOWIDTH 320
   #define VIDEOHEIGHT 240

   struct context {
       SDL_Renderer *renderer;
       SDL_Texture *texture;
       SDL_mutex *mutex;
       int n;
   };

   // VLC prepares to render a video frame.
   static void *lock(void *data, void **p_pixels) {

       struct context *c = (context *)data;

       int pitch;
       SDL_LockMutex(c->mutex);
       SDL_LockTexture(c->texture, NULL, p_pixels, &pitch);

       return NULL; // Picture identifier, not needed here.
   }

   // VLC just rendered a video frame.
   static void unlock(void *data, void *id, void *const *p_pixels) {

       struct context *c = (context *)data;

       uint16_t *pixels = (uint16_t *)*p_pixels;

       // We can also render stuff.
       int x, y;
       for(y = 10; y < 40; y++) {
           for(x = 10; x < 40; x++) {
               if(x < 13 || y < 13 || x > 36 || y > 36) {
                   pixels[y * VIDEOWIDTH + x] = 0xffff;
               } else {
                   // RV16 = 5+6+5 pixels per color, BGR.
                   pixels[y * VIDEOWIDTH + x] = 0x02ff;
               }
           }
       }

       SDL_UnlockTexture(c->texture);
       SDL_UnlockMutex(c->mutex);
   }

   // VLC wants to display a video frame.
   static void display(void *data, void *id) {

       struct context *c = (context *)data;

       SDL_Rect rect;
       rect.w = VIDEOWIDTH;
       rect.h = VIDEOHEIGHT;
       rect.x = (int)((1. + .5 * sin(0.03 * c->n)) * (WIDTH - VIDEOWIDTH) / 2);
       rect.y = (int)((1. + .5 * cos(0.03 * c->n)) * (HEIGHT - VIDEOHEIGHT) / 2);

       SDL_SetRenderDrawColor(c->renderer, 0, 80, 0, 255);
       SDL_RenderClear(c->renderer);
       SDL_RenderCopy(c->renderer, c->texture, NULL, &rect);
       SDL_RenderPresent(c->renderer);
   }

   static void quit(int c) {
       SDL_Quit();
       exit(c);
   }

   int main(int argc, char *argv[]) {

       libvlc_instance_t *libvlc;
       libvlc_media_t *m;
       libvlc_media_player_t *mp;
       char const *vlc_argv[] = {

           "--no-audio", // Don't play audio.
           "--no-xlib", // Don't use Xlib.

           // Apply a video filter.
           //"--video-filter", "sepia",
           //"--sepia-intensity=200"
       };
       int vlc_argc = sizeof(vlc_argv) / sizeof(*vlc_argv);

       SDL_Event event;
       int done = 0, action = 0, pause = 0, n = 0;

       struct context context;

       if(argc < 2) {
           printf("Usage: %s <filename>\n", argv[0]);
           return EXIT_FAILURE;
       }

       // Initialise libSDL.
       if(SDL_Init(SDL_INIT_VIDEO) < 0) {
           printf("Could not initialize SDL: %s.\n", SDL_GetError());
           return EXIT_FAILURE;
       }

       // Create SDL graphics objects.
       SDL_Window * window = SDL_CreateWindow(
               "Fartplayer",
               SDL_WINDOWPOS_UNDEFINED,
               SDL_WINDOWPOS_UNDEFINED,
               WIDTH, HEIGHT,
               SDL_WINDOW_SHOWN|SDL_WINDOW_RESIZABLE);
       if (!window) {
           fprintf(stderr, "Couldn't create window: %s\n", SDL_GetError());
           quit(3);
       }

       context.renderer = SDL_CreateRenderer(window, -1, 0);
       if (!context.renderer) {
           fprintf(stderr, "Couldn't create renderer: %s\n", SDL_GetError());
           quit(4);
       }

       context.texture = SDL_CreateTexture(
               context.renderer,
               SDL_PIXELFORMAT_BGR565, SDL_TEXTUREACCESS_STREAMING,
               VIDEOWIDTH, VIDEOHEIGHT);
       if (!context.texture) {
           fprintf(stderr, "Couldn't create texture: %s\n", SDL_GetError());
           quit(5);
       }

       context.mutex = SDL_CreateMutex();

       // If you don't have this variable set you must have plugins directory
       // with the executable or libvlc_new() will not work!
       printf("VLC_PLUGIN_PATH=%s\n", getenv("VLC_PLUGIN_PATH"));

       // Initialise libVLC.
       libvlc = libvlc_new(vlc_argc, vlc_argv);
       if(NULL == libvlc) {
           printf("LibVLC initialization failure.\n");
           return EXIT_FAILURE;
       }

       m = libvlc_media_new_path(libvlc, argv[1]);
       mp = libvlc_media_player_new_from_media(m);
       libvlc_media_release(m);

       libvlc_video_set_callbacks(mp, lock, unlock, display, &context);
       libvlc_video_set_format(mp, "RV16", VIDEOWIDTH, VIDEOHEIGHT, VIDEOWIDTH*2);
       libvlc_media_player_play(mp);

       // Main loop.
       while(!done) {

           action = 0;

           // Keys: enter (fullscreen), space (pause), escape (quit).
           while( SDL_PollEvent( &event )) {

               switch(event.type) {
                   case SDL_QUIT:
                       done = 1;
                       break;
                   case SDL_KEYDOWN:
                       action = event.key.keysym.sym;
                       break;
               }
           }

           switch(action) {
               case SDLK_ESCAPE:
               case SDLK_q:
                   done = 1;
                   break;
               case ' ':
                   printf("Pause toggle.\n");
                   pause = !pause;
                   break;
           }

           if(!pause) { context.n++; }

           SDL_Delay(1000/10);
       }

       // Stop stream and clean up libVLC.
       libvlc_media_player_stop(mp);
       libvlc_media_player_release(mp);
       libvlc_release(libvlc);

       // Close window and clean up libSDL.
       SDL_DestroyMutex(context.mutex);
       SDL_DestroyRenderer(context.renderer);

       quit(0);

       return 0;
   }
   </pre>

   ===Older API===

   This code was used for LibVLC 0.9.x and 1.0.x.

   <pre>
   /* libSDL and libVLC sample code
    * Copyright © 2008 Sam Hocevar <sam@zoy.org>
    * license: [http://en.wikipedia.org/wiki/WTFPL WTFPL] */

   #include <stdio.h>
   #include <stdint.h>
   #include <math.h>
   #include <stdlib.h>

   #include <SDL.h>
   #include <SDL_mutex.h>

   #include <vlc/vlc.h>

   #define WIDTH 640
   #define HEIGHT 480

   #define VIDEOWIDTH 320
   #define VIDEOHEIGHT 240

   struct ctx
   {
       SDL_Surface *surf;
       SDL_mutex *mutex;
   };

   static void catch (libvlc_exception_t *ex)
   {
       if(libvlc_exception_raised(ex))
       {
           fprintf(stderr, "exception: %s\n", libvlc_exception_get_message(ex));
           exit(1);
       }

       libvlc_exception_clear(ex);
   }

   #ifdef VLC09X
   static void * lock(struct ctx *ctx)
   {
       SDL_LockMutex(ctx->mutex);
       SDL_LockSurface(ctx->surf);
       return ctx->surf->pixels;
   }
   #else
   static void lock(struct ctx *ctx, void **pp_ret)
   {
       SDL_LockMutex(ctx->mutex);
       SDL_LockSurface(ctx->surf);
       *pp_ret = ctx->surf->pixels;
   }
   #endif



   static void unlock(struct ctx *ctx)
   {
       /* VLC just rendered the video, but we can also render stuff */
       uint16_t *pixels = (uint16_t *)ctx->surf->pixels;
       int x, y;

       for(y = 10; y < 40; y++)
           for(x = 10; x < 40; x++)
               if(x < 13 || y < 13 || x > 36 || y > 36)
                   pixels[y * VIDEOWIDTH + x] = 0xffff;
               else
                   pixels[y * VIDEOWIDTH + x] = 0x0;

       SDL_UnlockSurface(ctx->surf);
       SDL_UnlockMutex(ctx->mutex);
   }

   int main(int argc, char *argv[])
   {
       char clock[64], cunlock[64], cdata[64];
       char width[32], height[32], pitch[32];
       libvlc_exception_t ex;
       libvlc_instance_t *libvlc;
       libvlc_media_t *m;
       libvlc_media_player_t *mp;
       char const *vlc_argv[] =
       {
           "-q",
           //"-vvvvv",
           "--plugin-path", VLC_TREE "/modules",
           "--ignore-config", /* Don't use VLC's config files */
           "--noaudio",
           "--vout", "vmem",
           "--vmem-width", width,
           "--vmem-height", height,
           "--vmem-pitch", pitch,
           "--vmem-chroma", "RV16",
           "--vmem-lock", clock,
           "--vmem-unlock", cunlock,
           "--vmem-data", cdata,
       };
       int vlc_argc = sizeof(vlc_argv) / sizeof(*vlc_argv);

       SDL_Surface *screen, *empty;
       SDL_Event event;
       SDL_Rect rect;
       int done = 0, action = 0, pause = 0, n = 0;

       struct ctx ctx;

       /*
        *  Initialise libSDL
        */
       if(SDL_Init(SDL_INIT_VIDEO | SDL_INIT_EVENTTHREAD) == -1)
       {
           printf("cannot initialize SDL\n");
           return EXIT_FAILURE;
       }

       empty = SDL_CreateRGBSurface(SDL_SWSURFACE, VIDEOWIDTH, VIDEOHEIGHT,
                                    32, 0, 0, 0, 0);
       ctx.surf = SDL_CreateRGBSurface(SDL_SWSURFACE, VIDEOWIDTH, VIDEOHEIGHT,
                                       16, 0x001f, 0x07e0, 0xf800, 0);

       ctx.mutex = SDL_CreateMutex();

       int options = SDL_ANYFORMAT | SDL_HWSURFACE | SDL_DOUBLEBUF;

       screen = SDL_SetVideoMode(WIDTH, HEIGHT, 0, options);
       if(!screen)
       {
           printf("cannot set video mode\n");
           return EXIT_FAILURE;
       }

       /*
        *  Initialise libVLC
        */
       sprintf(clock, "%lld", (long long int)(intptr_t)lock);
       sprintf(cunlock, "%lld", (long long int)(intptr_t)unlock);
       sprintf(cdata, "%lld", (long long int)(intptr_t)&ctx);
       sprintf(width, "%i", VIDEOWIDTH);
       sprintf(height, "%i", VIDEOHEIGHT);
       sprintf(pitch, "%i", VIDEOWIDTH * 2);

       if(argc < 2)
       {
           printf("too few arguments (MRL needed)\n");
           return EXIT_FAILURE;
       }
       libvlc_exception_init(&ex);
       libvlc = libvlc_new(vlc_argc, vlc_argv, &ex);
       catch(&ex);
       m = libvlc_media_new(libvlc, argv[1], &ex);
       catch(&ex);
       mp = libvlc_media_player_new_from_media(m, &ex);
       catch(&ex);
       libvlc_media_release(m);

       libvlc_media_player_play(mp, &ex);
       catch(&ex);

       /*
        *  Main loop
        */
       rect.w = 0;
       rect.h = 0;

       while(!done)
       { 
           action = 0;

           /* Keys: enter (fullscreen), space (pause), escape (quit) */
           while( SDL_PollEvent( &event ) ) 
           { 
               switch(event.type)
               {
               case SDL_QUIT:
                   done = 1;
                   break;
               case SDL_KEYDOWN:
                   action = event.key.keysym.sym;
                   break;
               }
           }

           switch(action)
           {
           case SDLK_ESCAPE:
               done = 1;
               break;
           case SDLK_RETURN:
               options ^= SDL_FULLSCREEN;
               screen = SDL_SetVideoMode(WIDTH, HEIGHT, 0, options);
               break;
           case ' ':
               pause = !pause;
               break;
           }

           rect.x = (int)((1. + .5 * sin(0.03 * n)) * (WIDTH - VIDEOWIDTH) / 2);
           rect.y = (int)((1. + .5 * cos(0.03 * n)) * (HEIGHT - VIDEOHEIGHT) / 2);

           if(!pause)
               n++;

           /* Blitting the surface does not prevent it from being locked and
            * written to by another thread, so we use this additional mutex. */
           SDL_LockMutex(ctx.mutex);
           SDL_BlitSurface(ctx.surf, NULL, screen, &rect);
           SDL_UnlockMutex(ctx.mutex);

           SDL_Flip(screen);
           SDL_Delay(10);

           SDL_BlitSurface(empty, NULL, screen, &rect);
       }

       /*
        * Stop stream and clean up libVLC
        */
       libvlc_media_player_stop(mp, &ex);
       catch(&ex);

       libvlc_media_player_release(mp);
       libvlc_release(libvlc);

       /*
        * Close window and clean up libSDL
        */
       SDL_DestroyMutex(ctx.mutex);
       SDL_FreeSurface(ctx.surf);
       SDL_FreeSurface(empty);

       SDL_Quit();

       return 0;
   }

`Category:LibVLC <Category:LibVLC>`__
