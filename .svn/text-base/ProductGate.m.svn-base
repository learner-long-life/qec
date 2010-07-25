%% -*- texinfo -*-
%% @deftypefn {Function file} {} ProductGate(@var{size},@var{gate},@var{targetv})
%% Function @code{ProductGate} generates operator of size equal 2^@var{size}.
%% Parameter @var{gate} is 2x2 basic operator (ex. Not). Paramter
%% @var{targetv} is list of indices of target qubits.
%%
%% @example 
%% @group
%% ProductGate(3,Not,[1,2])
%%  @result{}
%% 0  0  0  0  0  0  1  0
%% 0  0  0  0  0  0  0  1
%% 0  0  0  0  1  0  0  0
%% 0  0  0  0  0  1  0  0
%% 0  0  1  0  0  0  0  0
%% 0  0  0  1  0  0  0  0
%% 1  0  0  0  0  0  0  0
%% 0  1  0  0  0  0  0  0
%%
%% @end group
%% @end example
%%
%% @end deftypefn
%%
%% @seealso {ControledGate, Id, Not, H, Pase}
%%
%% Author: Piotr Gawron, Jaroslaw Miszczak
%% Created: 25 November 2003

function ret = ProductGate(n,gate,targetv)
if (nargin~=3)
	usage('ProductGate(n,gate,targetv)');
end

if (~isscalar(n))
	error('1st parameter should be scalar!');
end

s = size(gate);

if (s(1) ~= s(2)) 
	error('2nd parameter should be matrix 2x2!');
end

if (n < max(targetv))
	error('Operator acts on %d qubits, max target index is %d!', n, max(targetv));
end

if (min(targetv)<1)
	error('Qubit index less than 0!');
end

idx = 1;
lv = sort(targetv);
if (lv(1) == 1)
	tmp = gate;
	idx = idx+1;
else
	tmp = speye(2);
end

for i = 2:n

  if ((idx <= length(lv)) && (lv(idx) == i))
    tmp2 = kron(tmp,gate);
    idx = idx + 1;
  else
    tmp2 = kron(tmp,speye(2));
  end
  clear tmp;
  tmp = tmp2;
  clear tmp2;

end

ret = tmp;
