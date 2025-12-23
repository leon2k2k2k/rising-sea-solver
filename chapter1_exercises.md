# FOAG Chapter 1 Exercises

Extracted from Vakil's Foundations of Algebraic Geometry

## Exercise 1.1.A

**Page**: 30

**Content**:
A category in which each morphism is an isomorphismiscalledagroupoid. (Thisnotionisnotimportantinwhatwewill discuss. Thepointofthisexerciseistogiveyousomepracticewithcategories,by relatingthemtoanobjectyouknowwell.) (a)Aperversedefinitionofagroupis: agroupoidwithoneobject. Makesenseof this. (Similarly,incaseyoucare: aperversedefinitionofamonoidis: acategory withoneobject.) (b)Describeagroupoidthatisnotagroup.

---

## Exercise 1.1.B

**Page**: 30

**Content**:
If Aisanobjectinacategory C,showthattheinvertibleelements of Mor(A,A)formagroup(calledtheautomorphismgroupof A,denoted Aut(A)). Whataretheautomorphismgroupsoftheobjectsin Examples1.1.2and1.1.3?Show thattwoisomorphicobjectshaveisomorphicautomorphismgroups. (Forreaders withatopologicalbackground: if Xisatopologicalspace,thenthefundamental groupoid is the category where the objects are points of X, and the morphisms x yarepathsfromxtoy,uptohomotopy. Thentheautomorphismgroupof x isthe(pointed)fundamentalgroupϑ (X,x ). Inthecasewhere Xisconnected, 0 1 0 an→dϑ 1 (X)isnotabelian,thisillustratesthefactthatforaconnectedgroupoid— whosedefinitionyoucanguess—theautomorphismgroupsoftheobjectsareall isomorphic,butnotcanonicallyisomorphic.) 1.1.4. Example: abeliangroups. Theabeliangroups,alongwithgrouphomomor- phisms,formacategory Ab.

---

## Exercise 1.1.C

**Page**: 34

**Content**:
Let()∨∨: f.d.Vec f.d.Vec bethedoubledualfunctorfrom · k k thecategoryoffinite-dimensionalvectorspacesoverktoitself. Showthat()∨∨ · is naturally isomorphic to the identi→ty functor on f.d.Vec . (Without the finite- k dimensionalityhypothesis,weonlygetanaturaltransformationoffunctorsfrom idto()∨∨.) · Let V bethecategorywhoseobjectsarethek-vectorspacesknforeachn 0 ↘ (thereisonevectorspaceforeachn),andwhosemorphismsarelineartransfor- mations. Theobjectsof V canbethoughtofasvectorspaceswithbases,andthe morphismsasmatrices. Thereisanobviousfunctor V f.d.Vec ,aseachknisa k finite-dimensionalvectorspace. →

---

## Exercise 1.1.D

**Page**: 34

**Content**:
Show that V f.d.Vec gives an equivalence of categories, k bydescribingan“inverse”functor. (Recallthatwearebeingcavalieraboutset- theoretic assumptions, see Cautio→n 0.3.1, so feel free to simultaneously choose basesforeachvectorspaceinf.d.Vec . Tomakethisprecise,youwillneedtouse k Go¨del-Bernayssettheoryorelsereplacef.d.Vec withaverysimilarsmallcategory, k butwewon’tworryaboutthis.) 1.1.22. ωω Aside for experts. Your argument for Exercise 1.1.D will show that (moduloset-theoreticissues)thisdefinitionofequivalenceofcategoriesisthesame asanotheronecommonlygiven: acovariantfunctor F: A Bisanequivalence ofcategoriesifitisfullyfaithfulandeveryobjectof Bisisomorphictoanobject oftheform F(A)forsome A A (Fisessentiallysurjecti→ve,atermwewillnot ↑ need).

**References**:
- Exercise 1.1

---

## Exercise 1.2.A

**Page**: 35

**Content**:
Showthatanytwoinitialobjectsareuniquelyisomorphic. Show thatanytwofinalobjectsareuniquelyisomorphic. Inotherwords,ifaninitialobjectexists,itisuniqueuptouniqueisomorphism, andsimilarlyforfinalobjects. This(partially)justifiesthephrase“theinitialobject” rather than “an initial object”, and similarly for “the final object” and “the zero object”. (Convention: we often say “the”, not “a”, for anything defined up to uniqueisomorphism.)

---

## Exercise 1.2.B

**Page**: 35

**Content**:
Whataretheinitialandfinalobjectsin Sets,Rings,and Top(if theyexist)? Howaboutinthetwoexamplesof§1.1.9? 1.2.3. Localizationofringsandmodules. Anotherimportantexampleofadefi- nitionbyuniversalpropertyisthenotionoflocalizationofaring. Wefirstreview a constructive definition, and then reinterpret the notion in terms of universal property. Amultiplicativesubset Sofaring Aisasubsetclosedundermultipli- cationcontaining1. Wedefinearing S!1A. Theelementsof S!1Aareoftheform a/s where a A and s S, and where a /s = a /s if (and only if) for some 1 1 2 2 ↑ ↑ s S, s(s a !s a ) = 0. We define (a /s )+(a /s ) = (s a +s a )/(s s ), 2 1 1 2 1 1 2 2 2 1 1 2 1 2 ↑ and (a /s ) (a /s ) = (a a )/(s s ). (If you wish, you may check that this 1 1 2 2 1 2 1 2 ↗ equalityoffractionsreallyisanequivalencerelationandthetwobinaryoperations onfractionsarewell-definedonequivalenceclassesandmake S!1Aintoaring.)

---

## Exercise 1.2.C

**Page**: 36

**Content**:
Show that A S!1A is injective if and only if S contains no zerodivisors. (Azerodivisorofaring Aisanelementasuchthatthereisanonzero elementbwithab=0. Theother→elementsof Aarecallednon-zerodivisors. For example,aninvertibleelementisneverazerodivisor. Counter-intuitively,0isa zerodivisorineveryringbutthe0-ring. Moregenerally,if Misan A-module,then a Aisazerodivisorfor Mifthereisanonzerom Mwitham=0. Theother ↑ ↑ elementsof Aarecallednon-zerodivisorsfor M. Equivalently,andveryusefully, a A is a non-zerodivisor for M if and only if a : M M is an injection, or ↑ ↗ equivalentlyinthelanguageof§1.5,if → a 0 $$M ↓ $$M isexact.) If Aisanintegraldomainand S=A\{0},then S!1Aiscalledthefractionfield of A,whichwedenote K(A). Thepreviousexerciseshowsthat Aisasubringofits fractionfield K(A). Wenowreturntothecasewhere Aisageneral(commutative) ring.

**Mathematical Expressions**:
- ``
- ``
- `M ↓ `

---

## Exercise 1.2.D

**Page**: 36

**Content**:
Verifythat A S!1Asatisfiesthefollowinguniversalproperty: S!1Aisinitialamong A-algebras Bwhereeveryelementof Sissenttoaninvertible elementin B. (Recall: thedatao→f“an A-algebra B”and“aringmap A B”are the same.) Translation: any map A B where every element of S is sent to an invertibleelementmustfactoruniquelythrough A S!1A. Anothertra→nslation: aringmapoutof S!1Aisthesamet→hingasaringmapfrom Athatsendsevery elementof Stoaninvertibleelement. Furthermore,→an S!1A-moduleisthesame thingasan A-moduleforwhichs : M Misan A-moduleisomorphismforall ↗· s S. ↑ In fact, it is cleaner to define A S→!1A by the universal property, and to showthatitexists,andtousetheuniversalpropertytocheckvariousproperties S!1Ahas. Let’sgetsomepracticew→iththisbydefininglocalizationsofmodules byuniversalproperty. Suppose Misan A-module. Wedefinethe A-modulemap

---

## Exercise 1.2.E

**Page**: 37

**Content**:
Show that ϖ: M S!1M exists, by constructing something satisfying the universal property. Hint: define elements of S!1M to be of the formm/swherem Mands S,→andm 1 /s 1 = m 2 /s 2 ifandonlyifforsome ↑ ↑ s S,s(s m !s m )=0. Definetheadditivestructureby(m /s )+(m /s )= 2 1 1 2 1 1 2 2 ↑ (s m +s m )/(s s ),andthe S!1A-modulestructure(andhencethe A-module 2 1 1 2 1 2 structure)isgivenby(a /s ) (m /s )=(a m )/(s s ). 1 1 2 2 1 2 1 2 ·

---

## Exercise 1.2.F

**Page**: 37

**Content**:
(a) Show that localization commutes with finite products, or equivalently, with finite direct sums. In other words, if M , ..., M are A-modules, describe an 1 n isomorphism (of A-modules, and of S!1A-modules) S!1(M M ) 1 n ↗ ··· ↗ S!1M S!1M . 1 n ↗···↗ (b)Showthatlocalizationcommuteswitharbitrarydirectsums. → (c)Showthat“localizationdoesnotnecessarilycommutewithinfiniteproducts”: theobviousmap S!1( M ) S!1M inducedbytheuniversalpropertyof i i i i localizationisnotalwaysanisomorphism. (Hint: (1,1/2,1/3,1/4,...) Q Q ↓ ↓ ↑ ↗ ↗ .) → ··· 1.2.4. Remark. Localization does not always commute with Hom, see Exam- ple1.5.10. But Exercise1.5.Hwillshowthatingoodsituations(ifthefirstargument of Homisfinitelypresented),localizationdoescommutewith Hom. 1.2.5. Tensor products. Another important example of a universal property constructionisthenotionofatensorproductof A-modules : obj(Mod ) obj(Mod ) $$obj(Mod ) A A A A ⇒ ↗ (M,N)! $$M N A ⇒ The subscript A is often suppressed when it is clear from context. The tensor productisoftendefinedasfollows. Supposeyouhavetwo A-modules Mand N. Thenelementsofthetensorproduct M Narefinite A-linearcombinationsof A ⇒ symbolsm n(m M,n N),subjecttorelations(m +m ) n=m n+m n, 1 2 1 2 ⇒ ↑ ↑ ⇒ ⇒ ⇒

**Mathematical Expressions**:
- ``
- ``
- `obj(Mod ) A A A A ⇒ ↗ (M,N)! `

---

## Exercise 1.2.I

**Page**: 38

**Content**:
Showthat(T,t: M N T)isuniqueuptouniqueisomorphism. ↗ Hint: firstfigureoutwhat“uniqueuptouniqueisomorphism”meansforsuch pairs,usingacategoryofpairs(T,t). The→nfollowtheanalogousargumentforthe product. In short: given M and N, there is an A-bilinear map t: M N M N, A ↗ ⇒ uniqueuptouniqueisomorphism,definedbythefollowinguniversalproperty:for →

---

## Exercise 1.2.J

**Page**: 39

**Content**:
Showthattheconstructionof§1.2.5satisfiestheuniversalproperty oftensorproduct. Thethreeexercisesbelowareusefulfactsabouttensorproductswithwhich youshouldbefamiliar. 1.2.K.IMPORTANTEXERCISE. (a) If M is an A-module and A B is a morphism of rings, give B M the A ⇒ structureofa B-module(thisispartoftheexercise). Showthatthisdescribesa functor Mod A Mod B . → (b)(tensorproductofrings)Iffurther A Cisanothermorphismofrings,show that B A Cha→sanaturalstructureofaring. Hint: multiplicationwillbegivenby ⇒ (b 1 c 1 )(b 2 c 2 )=(b 1 b 2 ) (c 1 c 2 ). (Exe→rcise1.2.Uwillinterpretthisconstruction ⇒ ⇒ ⇒ asafiberedcoproduct.) 1.2.L. IMPORTANT EXERCISE. If S is a multiplicative subset of A and M is an A-module, describe a natural isomorphism (S!1A) M ∼ S!1M (as S!1A- A ⇒ ⇑ modulesandas A-modules). → 1.2.M.EXERCISE ( COMMUTES WITH ). Showthattensorproductscommute ⇒ ⇓ witharbitrarydirectsums: if Mand{N } areall A-modules,describeanisomor- i i I ↔ phism ∼ M ( N ) $$ (M N ). i I i i I i ⇒ ⇓ ↔ ⇓ ↔ ⇒ 1.2.6. Essential Example: Fiberedproducts. Supposewehavemorphismsα: X Zandβ: Y Z(inanycategory). Thenthefiberedproduct(orfibredproduct)is anobject X Z Y alongwithmorphismspr X : X Z Y Xandpr Y : X Z Y → Y, ↗ ↗ ↗ wherethetw→ocompositionsα pr X ,β pr Y : X Z Y Zagree,suchthatgiven ↔ ↔ ↗ anyobject W withmapsto Xand Y (whosecompositio→nsto Zagree),thesem→aps factorthroughsomeunique W X Z Y: → ↗ W → ! ↑ ’’ X Y **$$Y ↗ Z pr Y pr X ϖ )) %% %% ϑ X $$Z (Warning: thedefinitionofthefiberedproductdependsonαandβ,eventhough theyareomittedfromthenotation X Y.) Z ↗ Bytheusualuniversalpropertyargument,ifitexists,itisuniqueuptounique isomorphism. (Youshouldthinkthisthroughuntilitiscleartoyou.) Thustheuse ofthephrase“thefiberedproduct”(ratherthan“afiberedproduct”)isreasonable,

**Mathematical Expressions**:
- ``
- ``
- ``
- ` (M N ). i I i i I i ⇒ ⇓ ↔ ⇓ ↔ ⇒ 1.2.6. Essential Example: Fiberedproducts. Supposewehavemorphismsα: X Zandβ: Y Z(inanycategory). Thenthefiberedproduct(orfibredproduct)is anobject X Z Y alongwithmorphismspr X : X Z Y Xandpr Y : X Z Y → Y, ↗ ↗ ↗ wherethetw→ocompositionsα pr X ,β pr Y : X Z Y Zagree,suchthatgiven ↔ ↔ ↗ anyobject W withmapsto Xand Y (whosecompositio→nsto Zagree),thesem→aps factorthroughsomeunique W X Z Y: → ↗ W → ! ↑ ’’ X Y **`

---

## Exercise 1.2.O

**Page**: 40

**Content**:
If Xisatopologicalspace,showthatfiberedproductsalways exist in the category of open sets of X, by describing what a fibered product is. (Hint: ithasaone-worddescription.)

---

## Exercise 1.2.P

**Page**: 40

**Content**:
If Zisthefinalobjectinacategory C,and X,Y C,showthat ↑ “X Y = X Y”: “the”fiberedproductover Zisuniquelyisomorphicto“the” Z ↗ ↗ product. Assumeallrelevant(fibered)productsexist. (Thisisanexerciseabout unwindingthedefinition.) 1.2.Q. USEFUL EXERCISE: TOWERS OF CARTESIAN DIAGRAMS ARE CARTESIAN DIAGRAMS. Ifthetwosquaresinthefollowingcommutativediagramare Cartesian diagrams,showthatthe“outsiderectangle”(involving U,V,Y,and Z)isalsoa Cartesiandiagram. U $$V %% %% W $$X %% %% Y $$Z

**Mathematical Expressions**:
- ``
- ``
- ``
- `V %% %% W `

---

## Exercise 1.2.R

**Page**: 40

**Content**:
Givenmorphisms X 1 Y,X 2 Y,and Y Z,showthatthere isanaturalmorphism X X X X ,assumingthatbothfiberedproducts 1 Y 2 1 Z 2 ↗ ↗ exist. (Thisistrivialonceyoufigureoutw→hatitis→saying. The→pointofthisexercise istoseewhyitistrivial.) →

---

## Exercise 1.2.T

**Page**: 41

**Content**:
Showthatcoproductfor Setsisdisjointunion. Thi↔siswhywe usethenotation fordisjointunion.

---

## Exercise 1.2.U

**Page**: 41

**Content**:
↔Suppose A B and A C are two ring morphisms, so in particular Band Care A-modules. Recall(Exercise1.2.K)that B Chasaring A ⇒ structure. Showthatthereisana→turalmorph→ism B B A Cgivenbyb b 1. ⇒ ⇐ ⇒ (Thisisnotnecessarilyaninclusion;see Exercise1.2.G.)Similarly,thereisanatural morphism C B A C. Showthatthisgivesafibere→dcoproductonrings,→i.e.,that ⇒ B C++ C → ⇒,, A ,, B++ A satisfiestheuniversalpropertyoffiberedcoproduct. 1.2.9. Monomorphismsandepimorphisms. 1.2.10. Definition. A morphism ϑ: X Y is a monomorphism if any two morphisms µ : Z X and µ : Z X such that ϑ µ = ϑ µ must satisfy 1 2 1 2 ↔ ↔ µ 1 =µ 2 . Inotherwords,thereisatmoston→ewayoffillinginthedottedarrowso thatthediagram → → Z 1 ↗ %% -- X $$Y π commutes — for any object Z, the natural map Mor(Z,X) Mor(Z,Y) is an injection. Intuitively,itisthecategoricalversionofaninjectivemap,andindeed thisnotiongeneralizesthefamiliarnotionofinjectivemapso→fsets. (Thereason wedon’tusetheword“injective”isthatinsomecontexts,“injective”willhave anintuitivemeaningwhichmaynotagreewith“monomorphism”. Oneexample: in the category of divisible groups, the map Q Q/Z is a monomorphism but →

**Mathematical Expressions**:
- ``

---

## Exercise 1.2.V

**Page**: 42

**Content**:
Showthatthecompositionoftwomonomorphismsisamonomor- phism.

---

## Exercise 1.2.W

**Page**: 42

**Content**:
Provethatamorphismϑ: X Y isamonomorphismifand only if the fibered product X X exists, and the induced diagonal morphism Y ↗ φ π : X X Y X(Definition1.2.7)isanisomorphi→sm. Wemaythentakethisasthe ↗ definitionofmonomorphism.(Monomorphismsaren’tcentraltofuturediscussions, althou→ghtheywillcomeupagain. Thisexerciseisjustgoodpractice.) 1.2.X.EASYEXERCISE. Weusethenotationof Exercise1.2.R.Showthatif Y Z isamonomorphism,thenthemorphism X X X X youdescribedin 1 Y 2 1 Z 2 ↗ ↗ Exercise1.2.Risanisomorphism. (Hint: foranyobject V,giveanaturalbijec→tion betweenmapsfrom V tothefirstandmapsfrom V to→thesecond. Itisalsopossible tousethe Diagonal-Base-Changediagram,Exercise1.2.S.) Thenotionofanepimorphismis“dual”tothedefinitionofmonomorphism, whereallthearrowsarereversed. Thisconceptwillnotbecentralforus,although itturnsupinthedefinitionofanabeliancategory. Intuitively,itisthecategorical versionofasurjectivemap. (Butbecarefulwhenworkingwithcategoriesofobjects that are sets with additional structure, as epimorphisms need not be surjective. Example: in the category Rings, Z Q is an epimorphism, but obviously not surjective.) → 1.2.11. Representablefunctorsand Yoneda’s Lemma. Muchofourdiscussion about universal properties can be cleanly expressed in terms of representable functors,undertherubricof“Yoneda’s Lemma”. Yoneda’slemmaisaneasyfact statedinacomplicatedway. Informallyspeaking,youcanessentiallyrecoveran objectinacategorybyknowingthemapsintoit. Forexample,wehaveseenthat thedataofmapsto X Yarenaturally(canonically)thedataofmapsto Xandto Y. ↗ Indeed,wehavenowtakenthisasthedefinitionof X Y. ↗ Recall Example1.1.20. Suppose Aisanobjectofcategory C. Foranyobject C C,wehaveasetofmorphisms Mor(C,A). Ifwehaveamorphismf: B C, ↑ wegetamapofsets → (1.2.11.1) Mor(C,A) $$Mor(B,A), bycomposition: givenamapfrom Cto A,wegetamapfrom Bto Abyprecom- posing with f: B C. Hence this gives a contravariant functor h : C Sets. A Yoneda’s Lemma states that the functor h determines A up to unique isomor- A phism. Morepreci→sely: → 1.2.Y.IMPORTANTEXERCISETHATYOUSHOULDDOONCEINYOURLIFE(YONEDA’S LEMMA). (a)Supposeyouhavetwoobjects Aand A inacategory C,andmaps → (1.2.11.2) i : Mor(C,A) $$Mor(C,A ) C → that commute with the maps (1.2.11.1). Show that the i (as C ranges over the C objects of C) are induced from a unique morphism g: A A . More precisely, → →

**Mathematical Expressions**:
- ``
- ``
- `Mor(B,A), bycomposition: givenamapfrom Cto A,wegetamapfrom Bto Abyprecom- posing with f: B C. Hence this gives a contravariant functor h : C Sets. A Yoneda’s Lemma states that the functor h determines A up to unique isomor- A phism. Morepreci→sely: → 1.2.Y.IMPORTANTEXERCISETHATYOUSHOULDDOONCEINYOURLIFE(YONEDA’S LEMMA). (a)Supposeyouhavetwoobjects Aand A inacategory C,andmaps → (1.2.11.2) i : Mor(C,A) `

---

## Exercise 1.3.D

**Page**: 46

**Content**:
(a)Interpretthestatement“Q=colim 1 Z”. n (b) Interpret the union of some subsets of a given set as a colimit. (Dually, the intersectioncanbeinterpretedasalimit.) Theobjectsofthecategoryinquestion arethesubsetsofthegivenset.

---

## Exercise 1.3.E

**Page**: 47

**Content**:
Suppose I isfiltered. (Wewillalmostexclusivelyusethecase where I isafilteredset.) Recallthesymbol fordisjointunionofsets. Showthat anydiagramin Setsindexedby I hasthefollowing,withtheobviousmapstoit, ↔ asacolimit: (a ,i)∼(a ,j)ifandonlyiftherearef: A A and (a ,i) A i j i k i i ↑ g: A A inthediagramforwhichf(a )=g(a )in A ⇐ i ⇒↔ I ⇑!" j k i → j k# (Youwillseethatthe“filtered”hypothesisisthereistoensurethat∼isanequiva- → lencerelation.) For example, in Example 1.3.7, each element of the colimit is an element of something upstairs, but you can’t say in advance what it is an element of. For instance,17/125isanelementofthe5!3 Z(or5!4 Z,orlaterones),butnot5!2 Z. Thisideaappliestomanycategorieswhoseobjectscanbeinterpretedassets withadditionalstructure(suchasabeliangroups,A-modules,groups,etc.). For example,thecolimitcolim M inthecategoryof A-modules Mod canbedescribed i A as follows. The set underlying colim M is defined as in Exercise 1.3.E. To add i theelementsm M andm M ,choosean) I witharrowsu: i )and i i j j ↑ ↑ ↑ v: j ),andthendefinethesumofm andm tobe F(u)(m )+F(v)(m ) M . i j i j & ↑ → →

**References**:
- Example 1.3.7
- Exercise 1.3

---

## Exercise 1.3.F

**Page**: 48

**Content**:
Verifythatthe A-moduledescribedaboveisindeedthecolimit. (Make sure you verify that addition is well-defined, i.e., is independent of the choiceofrepresentativesm andm ,thechoiceof),andthechoiceofarrowsuand i j v. Similarly,makesurethatscalarmultiplicationiswell-defined.) 1.3.G. USEFUL EXERCISE (LOCALIZATION AS A COLIMIT). Generalize Exer- cise1.3.D(a)tointerpretlocalizationofanintegraldomainasacolimitoverafiltered set: suppose Sisamultiplicativesetof A,andinterpret S!1A=colim1Awhere s thecolimitisovers S,andinthecategoryof A-modules. (Aside: Canyoumake ↑ someversionofthisworkevenif Aisn’tanintegraldomain,e.g.,S!1A=colim A ? s Thiswillworkinthecategoryof A-algebras.) Avariantofthisconstructionworkswithoutthefilteredcondition,ifyouhave anothermeansof“connectingelementsindifferentobjectsofyourdiagram”. For example: 1.3.H.EXERCISE: COLIMITSOFA-MODULESWITHOUTTHEFILTEREDCONDITION. Suppose you are given a diagram of A-modules indexed by I: F: I Mod , A wherewelet M := F(i). Showthatthecolimitis M modulotherelations i ⇓ i ↔ I i m i !F(n)(m i )foreveryn: i jin I (i.e.,foreveryarrowinthediagram→). (Some- whatmoreprecisely: “modulo”means“quotientedbythesubmodulegenerated by”.) → 1.3.9. Summary. Oneusefulthingtoinformallykeepinmindisthefollowing. Ina categorywheretheobjectsare“set-like”,anelementofalimitcanbethoughtof asafamilyofelementsofeachobjectinthediagram,thatare“compatible”(Exer- cise1.3.C).Andanelementofacolimitcanbethoughtofas(“hasarepresentative thatis”)anelementofasingleobjectinthediagram(Exercise1.3.E).Eventhough thedefinitionsoflimitandcolimitarethesame,justwitharrowsreversed,these interpretationsarequitedifferent. 1.3.10. Smallremark. Infact,colimitsexistinthecategoryofsetsforallreasonable (“small”)indexcategories(seeforexample[E,Thm.A6.1]),butthatwon’tmatter tous. 1.3.11. Joke. Whatdoyoucallsomeonewhoreadsapaperoncategorytheory? Answer: Acoauthor. 1.4Adjoints Wenextcometoaveryusefulnotioncloselyrelatedtouniversalproperties. Justasauniversalproperty“essentially”(uptouniqueisomorphism)determines an object in a category (assuming such an object exists), “adjoints” essentially determineafunctor(again,assumingitexists). Twocovariantfunctors F: A B →

---

## Exercise 1.4.A

**Page**: 49

**Content**:
Writedownwhatthisdiagramshouldbe. →

---

## Exercise 1.4.B

**Page**: 49

**Content**:
Show that the map τ AB (1.4.0.1) has the following properties. For each A there is a map η : A GF(A) so that for any g: F(A) B, the A correspondingτ (g): A G(B)isgivenbythecomposition AB → → A ηA $$GF(A) Gg $$G(B). → Similarly,thereisamap, : FG(B) Bforeach Bsothatforanyf: A G(B), B thecorrespondingmapτ!1(f): F(A) Bisgivenbythecomposition AB → → F(A) Ff $$FG(B) )B $$B. → Hereisakeyexampleofanadjointpair.

**Mathematical Expressions**:
- ``
- ``
- ``
- ``
- `GF(A) Gg `
- `FG(B) )B `

---

## Exercise 1.4.C

**Page**: 49

**Content**:
Suppose M,N,and Pare A-modules(where Aisaring).Describe abijection Hom (M N,P) Hom (M,Hom (N,P)). (Hint: trytousethe A A A A ⇒ universalpropertyof .) ⇒ ⇓ 1.4.D.EXERCISE(TENSOR-HOMADJUNCTION). Showthat() A Nand Hom A (N, ) · ⇒ · areadjointfunctors.

---

## Exercise 1.4.E

**Page**: 49

**Content**:
Suppose B Aisamorphismofrings. If Misan A-module,you cancreatea B-module M byconsideringitasa B-module. Thisgivesafunctor B B : Mod A Mod B . Showtha→tthisfunctorisright-adjointto B A. Inotherwords, · ·⇒ describeabijection → Hom (N A,M)= ∼ Hom (N,M ) A B B B ⇒ functorialinbotharguments. (Thisadjointpairisveryimportant.) 1.4.1. ωFancierremarkswewon’tuse. Youcancheckthattheleftadjointdetermines therightadjointuptonaturalisomorphism,andviceversa.Themapsη and, of A B Exercise1.4.Barecalledtheunitandcounitoftheadjunction.Thisleadstoadifferent characterizationofadjunction. Supposefunctors F: A B and G: B A are given,alongwithnaturaltransformationsη: id GFand,: FG id withthe A B propertythat G, ↔ ηG=id G (foreach B ↑ B,thecomp→ositionofη G(B) : → G(B) → → →

---

## Exercise 1.4.G

**Page**: 50

**Content**:
Constructthe“groupificationfunctor”Hfromthecategoryof nonemptyabeliansemigroupstothecategoryofabeliangroups. (Onepossible construction: given an abelian semigroup S, the elements of its groupification H(S)areorderedpairs(a,b) S S,whichyoumaythinkofasa!b,withthe ↑ ↗ equivalencethat(a,b) ∼ (c,d)ifa+d+e = b+c+eforsomee S. Describe ↑ additioninthisgroup,andshowthatitsatisfiesthepropertiesofanabeliangroup. Describetheabeliansemigroupmap S H(S).) Let Fbetheforgetfulfunctorfrom thecategoryofabeliangroups Abtothecategoryofabeliansemigroups. Showthat Hisleft-adjointto F. →

---

## Exercise 1.5.A

**Page**: 56

**Content**:
Describeexactsequences (1.5.6.4) 0 $$imfi $$Ai+1 $$cokerfi $$0 0 $$Hi(A ) $$cokerfi!1 $$imfi $$0 • (Thesearesomehowdualto(1.5.6.3). Infactinsomemirroruniversethismight havebeengivenasthestandarddefinitionofhomology.) Assumethecategoryis thatofmodulesoverafixedringforconvenience,butbeawarethattheresultis trueforanyabeliancategory. 1.5.B.EXERCISEANDIMPORTANTDEFINITION. Suppose 0 d0 $$A1 d1 $$ dn!1 $$An dn $$$$0 ··· isacomplexoffinite-dimensionalk-vectorspaces(oftencalled A forshort).Define • hi(A ) := dim Hi(A ). Showthat (!1)idim Ai = (!1)ihi(A ). Inparticular, • • • if A isexact,then (!1)idim Ai =0. (Ifyouhaven’tdealtmuchwithcohomol- • ⇔ ⇔ ogy,thiswillgiveyousomepractice.) ⇔ 1.5.C. IMPORTANT EXERCISE. Suppose C is an abelian category. Define the category Com ofcomplexes)asfollows. Theobjectsareinfinitecomplexes C A : $$Ai!1 fi!1 $$Ai fi $$Ai+1 fi+1 $$ • ··· ···

**Mathematical Expressions**:
- ``
- ``
- ``
- ``
- ``
- ``
- ``
- ``
- ``
- ``
- ``
- ``
- ``
- ``
- ``
- ``
- ``
- `imfi `
- `cokerfi `
- `Hi(A ) `
- `imfi `
- `A1 d1 `
- `An dn `
- `0 ··· isacomplexoffinite-dimensionalk-vectorspaces(oftencalled A forshort).Define • hi(A ) := dim Hi(A ). Showthat (!1)idim Ai = (!1)ihi(A ). Inparticular, • • • if A isexact,then (!1)idim Ai =0. (Ifyouhaven’tdealtmuchwithcohomol- • ⇔ ⇔ ogy,thiswillgiveyousomepractice.) ⇔ 1.5.C. IMPORTANT EXERCISE. Suppose C is an abelian category. Define the category Com ofcomplexes)asfollows. Theobjectsareinfinitecomplexes C A : `
- `Ai fi `

---

## Exercise 1.5.E

**Page**: 57

**Content**:
Showthattwohomotopicmapsgivethesamemaponhomology. → 1.5.8. Theorem(Longexactsequences). — Ashortexactsequenceofcomplexes 0 : $$0 $$0 $$0 $$ • ··· ··· A %% : $$Ai! %% 1 fi!1 $$A %% i fi $$Ai+ %% 1 fi+1 $$ • ··· ··· %% %% gi!1 %% gi %% gi+1 B : $$Bi!1 $$Bi $$Bi+1 $$ • ··· ··· C %% : $$Ci! %% 1 hi!1 $$C %% i hi $$Ci+ %% 1 hi+1 $$ • ··· ··· %% %% %% %% 0 : $$0 $$0 $$0 $$ • ··· ··· inducesalongexactsequenceincohomology $$Hi!1(C ) $$ • ··· Hi(A ) $$Hi(B ) $$Hi(C ) $$ • • • Hi+1(A ) $$ • ···

**Mathematical Expressions**:
- ``
- ``
- ``
- ``
- ``
- ``
- ``
- ``
- ``
- ``
- ``
- ``
- ``
- ``
- ``
- ``
- ``
- ``
- ``
- ``
- ``
- ``
- ``
- ``
- ``
- ``
- `0 `
- `0 `
- `Ai! %% 1 fi!1 `
- `Ai+ %% 1 fi+1 `
- `Bi!1 `
- `Bi+1 `
- `Ci! %% 1 hi!1 `
- `Ci+ %% 1 hi+1 `
- `0 `
- `0 `
- `Hi!1(C ) `
- `Hi(B ) `
- ` • • • Hi+1(A ) `

---

## Exercise 1.5.F

**Page**: 58

**Content**:
Suppose Fisanexactfunctor. Showthatapplying Ftoanexact sequencepreservesexactness. Forexample,if Fiscovariant,and A A A is → →→ exact,then FA FA FA isexact. (Thiswillbegeneralizedin Exercise1.5.I(c).) → →→ → →

---

## Exercise 1.5.G

**Page**: 58

**Content**:
Suppose Aisaring,S Aisamultiplicativesubset,and Mis → → ≃ an A-module. (a)Showthatlocalizationof A-modules Mod Mod isanexactcovariant A S!1A functor. (b)Showthat() A Misaright-exactcovariant→functor Mod A Mod A . (Thisisa · ⇒ repeatof Exercise1.2.H.) (c)Showthat Hom(M, )isaleft-exactcovariantfunctor Mod A→ Mod A . If C is · any abelian category, and C C, show that Hom(C, ) is a left-exact covariant ↑ · functor C Ab. → (d)Showthat Hom(,M)isaleft-exactcontravariantfunctor Mod Mod .If C is A A · anyabelian→category,and C C,showthat Hom(,C)isaleft-exactcontravariant ↑ · functor C Ab. → →

---

## Exercise 1.5.H

**Page**: 59

**Content**:
Suppose Misafinitelypresented A-module: Mhasafinite numberofgenerators,andwiththesegeneratorsithasafinitenumberofrelations; orusefullyequivalently,fitsinanexactsequence (1.5.9.1) A q $$A p $$M $$0 ⇐ ⇐ Use(1.5.9.1)andtheleft-exactnessof Homtodescribeanisomorphism S!1Hom (M,N)++ ∼ $$Hom (S!1M,S!1N). A S!1A (Youmightbeabletointerpretthisinlightofavariantof Exercise1.5.Ibelow,for left-exactcontravariantfunctorsratherthanright-exactcovariantfunctors.) 1.5.10. Example: Homdoesn’talwayscommutewithlocalization. Inthelanguageof Exercise1.5.H,take A=N=Z,M=Q,and S=Z\{0}. 1.5.11. ωTwousefulfactsinhomologicalalgebra. We now come to two (sets of) facts I wish I had learned as a child, as they would have saved me lots of grief. They encapsulate what is best and worst of abstractnonsense. Thestatementsaresogeneralastobenonintuitive. Theproofs areveryshort. Theygeneralizesomespecificbehaviorthatiseasytoproveonan adhocbasis. Oncetheyaresecondnaturetoyou,manysubtlefactswillbecome obvioustoyouasspecialcases. Andyouwillseethattheywillgetused(implicitly orexplicitly)repeatedly. 1.5.12. ωInteractionofhomologyand(right/left-)exactfunctors. Youmightwaittoprovethisuntilyoulearnaboutcohomologyin Chapter18, whenitwillfirstbeusedinaseriousway. 1.5.I. IMPORTANT EXERCISE (THE FHHF THEOREM). This result can take you far, and perhaps for that reason it has sometimes been called the Fernbahnhof (Fernba Hn Ho F)Theorem,notablyin[Vak1,Exer.1.5.I].Suppose F: A B isa covariantfunctorofabeliancategories,and C isacomplexin A. • (a) (Fright-exactyields FH • $$H • F)If Fisright-exact,describe→anatural morphism FH H F.(Moreprecisely,foreachi,theleftsideis Fapplied • • tothecohomologyatpieceiof C ,whiletherightsideisthecohomology • atpieceiof FC •→.) (b) (F left-exact yields FH • ++ H • F) If F is left-exact, describe a natural morphism H F FH . • • ∼ (c) (Fexactyields FH • ++ $$H • F)If Fisexact,showthatthemorphismsof (a)and(b)arein→versesandthusisomorphisms. Hint for (a): use Ci di $$Ci+1 $$cokerdi $$0 to give an isomorphism Fcokerdi ∼ coker Fdi. Thenusethefirstlineof(1.5.6.4)togiveanepimorphism Fimdi ↫ im Fdi. Then use the second line of (1.5.6.4) to give the desired map FHi C • H↑ i →FC • . Whileyouareatit,youmayaswelldescribeamapforthefourth memberofthequartet{coker,im,H,ker}: Fkerdi ker Fdi. → 1.5.13. Ifthismakesyourheadspin,youmayprefertothinkofitinthefollowing → specificcase,whereboth A and Barethecategoryof A-modules,and Fis() N A · ⇒ for some fixed A-module N. Your argument in this case will translate without

**Mathematical Expressions**:
- ``
- ``
- ``
- ``
- ``
- ``
- ``
- ``
- ``
- `A p `
- `0 ⇐ ⇐ Use(1.5.9.1)andtheleft-exactnessof Homtodescribeanisomorphism S!1Hom (M,N)++ ∼ `
- `H • F)If Fisright-exact,describe→anatural morphism FH H F.(Moreprecisely,foreachi,theleftsideis Fapplied • • tothecohomologyatpieceiof C ,whiletherightsideisthecohomology • atpieceiof FC •→.) (b) (F left-exact yields FH • ++ H • F) If F is left-exact, describe a natural morphism H F FH . • • ∼ (c) (Fexactyields FH • ++ `
- `Ci+1 `

---

## Exercise 1.5.K

**Page**: 60

**Content**:
Makesenseofthestatementthat“limitscommutewithlimits”in ageneralcategory,andproveit. (Hint: recallthatkernelsarelimits. Theprevious exerciseshouldbeacorollaryofthisone.) 1.5.17. Proposition (right adjoints commute with limits). — Suppose (F: C D,G: D C)isapairofadjointfunctors. If A = lim A isalimitin D ofadiagram i → →

---

## Exercise 1.5.L

**Page**: 61

**Content**:
Showthatin Mod A ,colimitsoverfilteredindexcategoriesare exact. (Yourargumentwillapplywithoutchangetoanyabeliancategorywhose objects can be interpreted as “sets with additional structure”.) Right-exactness follows from the above discussion, so the issue is left-exactness. (Possible hint: Afteryoushowthatlocalizationisexact,Exercise1.5.G(a),orstalkificationisexact, Exercise2.6.E,inahands-onway,youwillbeeasilyabletoprovethis. Conversely, ifyoudothisexercise,thosetwowillbeeasy.)

---

## Exercise 1.5.M

**Page**: 61

**Content**:
Showthatfilteredcolimitscommutewithhomologyin Mod A . Hint: usethe FHHFTheorem(Exercise1.5.I),andtheprevious Exercise. Inlightof Exercise1.5.M,youmaywanttothinkabouthowlimits(andcolimits) commutewithhomologyingeneral,andwhichwaymapsgo. Thestatementof the FHHFTheoremshouldsuggesttheanswer. (Arelimitsanalogoustoleft-exact functors,orright-exactfunctors?) Wewon’tdirectlyusethisinsight,butsee§18.1 (vii)foranexample. Justascolimitsareexact(notjustright-exact)inespeciallygoodcircumstances, limitsareexact(notjustleft-exact)too. Thefollowingwillbeusedtwicein Chap- ter28.

---

## Exercise 1.5.N

**Page**: 62

**Content**:
Suppose . . . . . . . . . %%%% %% %% 0 $$A $$B $$C $$0 n+1 n+1 n+1 %%%% %% %% 0 $$A $$B $$C $$0 n n n %%%% %% %% . . . . . . . . . %%%% %% %% 0 $$A $$B $$C $$0 0 0 0 is an inverse system of exact sequences of modules over a ring, such that the maps A A are surjective. (We say: “transitionmaps of theleft term are n+1 n surjective”.) Showthatthelimit → (1.5.17.1) 0 $$lim A $$lim B $$lim C $$0 n n n isalsoexact. (Youwillneedtodefinethemapsin(1.5.17.1).) 1.5.18. Unimportant Remark. Basedontheseideas,youmaysuspectthatright-exact functorsalwayscommutewithcolimits. Thefactthattensorproductcommutes withinfinitedirectsums(Exercise1.2.M)mayreinforcethisidea. Unfortunately, itisnottrue—“doubledual” ∨∨ : Vec Vec iscovariantandrightexact(in k k · fact,exact),butdoesnotcommutewithinfinitedirectsums,as (k∨∨)isnot ⇓i=1 isomorphicto( ⇓i=1 k)∨∨. → → → 1.5.19. ωDreamingofderivedfunctors. Whenyouseealeft-exactfunctor,you shouldalwaysdreamthatyouareseeingtheendofalongexactsequence. If 0 $$M $$M $$M $$0 → →→ isanexactsequenceinabeliancategory A,and F: A Bisaleft-exactfunctor, then 0 $$FM $$FM $$FM→ → →→ isexact,andyoushouldalwaysdreamthatitshouldcontinueinsomenaturalway. Forexample,thenexttermshoulddependonlyon M ,callit R1FM ,andifitis → → zero,then FM FM isanepimorphism. Thisremarkholdstrueforleft-exact →→ andcontravariantfunctorstoo. Ingoodcases,suchacontinuationexists,andis incrediblyusefu→l. Wewilldiscussthisin Chapter23. 1.6ωSpectralsequences

**Mathematical Expressions**:
- ``
- ``
- ``
- ``
- ``
- ``
- ``
- ``
- ``
- ``
- ``
- ``
- ``
- ``
- ``
- ``
- ``
- ``
- ``
- ``
- ``
- ``
- ``
- `A `
- `C `
- `A `
- `C `
- `A `
- `C `
- `lim A `
- `lim C `
- `M `
- `M `
- `FM `

---

## Exercise 1.6.F

**Page**: 70

**Content**:
Usespectralsequencestoshowthatashortexactsequenceof complexesgivesalongexactsequenceincohomology(Theorem1.5.8). (Thisisa generalizationof Exercise1.6.E.) The Grothendieckcomposition-of-functorsspectralsequence(Theorem23.3.5) willbeanimportantexampleofaspectralsequencethatspecializesinanumberof usefulways. Youarenowreadytogooutintotheworldandusespectralsequencestoyour heart’scontent! 1.6.7. Completedefinitionofspectralsequences,andproof. You should most definitely not read the precise definition of a spectral se- quence,andtheproofthattheyworkasadvertised,anytimesoonafterreadingthe introductiontospectralsequencesabove. Butafterasuitableinterval,youshould at least flip through a construction and proof to convince yourself that nothing fancyisinvolved. Theideaisnotasbadasyoumightthink,see[Vak2]. Itisusefultonoticethattheproofimpliesthatspectralsequencesarefunctorial inthe0thpage: thespectralsequenceformalismhasgoodfunctorialpropertiesin thedoublecomplex. Unfortunately,Grothendieck’sterminology“spectralfunctor” [Gr1,§2.4]didnotcatchon.

---

