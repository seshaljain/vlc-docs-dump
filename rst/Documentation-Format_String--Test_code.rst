.. raw:: mediawiki

   {{Example code|for=Documentation:Format String|l=Expat}}

This `command-line <command-line>`__ example runs through `format strings <Documentation:Format_String>`__ in the space ``/[$%][A-Z_a-z]/`` as a test (or novelty). It should work for VLC 3.0.x under Windows or \*nix, provided that ``vlc`` is the path to VLC

-  Windows users can change to the directory of VLC or replace ``vlc`` with
-  macOS users can set a Bash variable or replace ``vlc`` with

``BigBuckBunny.ogv`` can be replaced with a video of your choice. The format strings cover the screen for three seconds, then VLC exits; invalid sequences will render as literal strings.

.. code:: winbatch

   vlc -I dummy '--sub-source=marq{marquee="A[$A] B[$B] C[$C] D[$D] E[$E] F[$F] G[$G] H[$H] I[$I] J[$J] K[$K] L[$L] M[$M] N[$N] O[$O] P[$P] Q[$Q] R[$R] S[$S] T[$T] U[$U] V[$V] W[$W] X[$X] Y[$Y] Z[$Z] a[$a] b[$b] c[$c] d[$d] e[$e] f[$f] g[$g] h[$h] i[$i] j[$j] k[$k] l[$l] m[$m] n[$n] o[$o] p[$p] q[$q] r[$r] s[$s] t[$t] u[$u] v[$v] w[$w] x[$x] y[$y] z[$z] _[$_] A[%A] B[%B] C[%C] D[%D] E[%E] F[%F] G[%G] H[%H] I[%I] J[%J] K[%K] L[%L] M[%M] N[%N] O[%O] P[%P] Q[%Q] R[%R] S[%S] T[%T] U[%U] V[%V] W[%W] X[%X] Y[%Y] Z[%Z] _[%_] a[%a] b[%b] c[%c] d[%d] e[%e] f[%f] g[%g] h[%h] i[%i] j[%j] k[%k] l[%l] m[%m] n[%n] o[%o] p[%p] q[%q] r[%r] s[%s] t[%t] u[%u] v[%v] w[%w] x[%x] y[%y] z[%z]",position=5}' --start-time=0 --stop-time=3 --no-video-title-show BigBuckBunny.ogv vlc://quit

The code is written in the format \ ``X``\ \ ``[$``\ \ ``X``\ \ ``]`` with \ ``X``\ \ ``[]`` merely marking the code used to generate the rendered X. If you prefer:

.. code:: winbatch

   vlc -I dummy '--sub-source=marq{marquee="$A $B $C $D $E $F $G $H $I $J $K $L $M $N $O $P $Q $R $S $T $U $V $W $X $Y $Z $a $b $c $d $e $f $g $h $i $j $k $l $m $n $o $p $q $r $s $t $u $v $w $x $y $z $_ %A %B %C %D %E %F %G %H %I %J %K %L %M %N %O %P %Q %R %S %T %U %V %W %X %Y %Z %_ %a %b %c %d %e %f %g %h %i %j %k %l %m %n %o %p %q %r %s %t %u %v %w %x %y %z",position=5}' --start-time=0 --stop-time=3 --no-video-title-show BigBuckBunny.ogv vlc://quit
