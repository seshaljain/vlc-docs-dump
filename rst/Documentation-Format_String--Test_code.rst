{{Example codel=Expat}} This [[command-line]] example runs through
[[Documentation:Format Stringwindows}}</code> \* macOS users can set a
Bash variable or replace <code>vlc</code> with <code>{{Path to
VLC|mac}}</code>

<code>BigBuckBunny.ogv</code> can be replaced with a video of your
choice. The format strings cover the screen for three seconds, then VLC
exits; invalid sequences will render as literal strings.

<syntaxhighlight lang="winbatch"> vlc -I dummy
'--sub-source=marq{marquee="A[$A] B[$B] C[$C] D[$D] E[$E] F[$F] G[$G]
H[$H] I[$I] J[$J] K[$K] L[$L] M[$M] N[$N] O[$O] P[$P] Q[$Q] R[$R] S[$S]
T[$T] U[$U] V[$V] W[$W] X[$X] Y[$Y] Z[$Z] a[$a] b[$b] c[$c] d[$d] e[$e]
f[$f] g[$g] h[$h] i[$i] j[$j] k[$k] l[$l] m[$m] n[$n] o[$o] p[$p] q[$q]
r[$r] s[$s] t[$t] u[$u] v[$v] w[$w] x[$x] y[$y] z[$z] \_[$_] A[%A] B[%B]
C[%C] D[%D] E[%E] F[%F] G[%G] H[%H] I[%I] J[%J] K[%K] L[%L] M[%M] N[%N]
O[%O] P[%P] Q[%Q] R[%R] S[%S] T[%T] U[%U] V[%V] W[%W] X[%X] Y[%Y] Z[%Z]
\_[%_] a[%a] b[%b] c[%c] d[%d] e[%e] f[%f] g[%g] h[%h] i[%i] j[%j] k[%k]
l[%l] m[%m] n[%n] o[%o] p[%p] q[%q] r[%r] s[%s] t[%t] u[%u] v[%v] w[%w]
x[%x] y[%y] z[%z]",position=5}' --start-time=0 --stop-time=3
--no-video-title-show BigBuckBunny.ogv vlc://quit </syntaxhighlight>

The code is written in the format
<code><var>X</var>[$<var>X</var>]</code> with
<code><var>X</var>[]</code> merely marking the code used to generate the
rendered <var>X</var>. If you prefer: <syntaxhighlight lang="winbatch">
vlc -I dummy '--sub-source=marq{marquee="$A $B $C $D $E $F $G $H $I $J
$K $L $M $N $O $P $Q $R $S $T $U $V $W $X $Y $Z $a $b $c $d $e $f $g $h
$i $j $k $l $m $n $o $p $q $r $s $t $u $v $w $x $y $z $\_ %A %B %C %D %E
%F %G %H %I %J %K %L %M %N %O %P %Q %R %S %T %U %V %W %X %Y %Z %\_ %a %b
%c %d %e %f %g %h %i %j %k %l %m %n %o %p %q %r %s %t %u %v %w %x %y
%z",position=5}' --start-time=0 --stop-time=3 --no-video-title-show
BigBuckBunny.ogv vlc://quit </syntaxhighlight>
