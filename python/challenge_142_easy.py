"""
Falling-sand Games are particle-simulation games that focus on the interaction between 
particles in a 2D-world. Sand, as an example, might fall to the ground forming a pile.
Other particles might be much more complex, like fire, that might spread depending on 
adjacent particle types.

Your goal is to implement a mini falling-sand simulation for just sand and stone. The 
simulation is in 2D-space on a uniform grid, where we are viewing this grid from the side.
Each type's simulation properties are as follows:

  - Stone always stays where it was originally placed. It never moves.
  - Sand keeps moving down through air, one step at a time, until it either hits the 
    bottom of the grid, other sand, or stone.

Input Description
=================
On standard console input, you will be given an integer N which represents the N x N 
grid of ASCII characters. This means there will be N-lines of N-characters long. This 
is the starting grid of your simulated world: the character ' ' (space) means an 
empty space, while '.' (dot) means sand, and '#' (hash or pound) means stone. Once you 
parse this input, simulate the world until all particles are settled (e.g. the sand 
has fallen and either settled on the ground or on stone). "Ground" is defined as the 
solid surface right below the last row.

Output Description
==================
Print the end result of all particle positions using the input format for particles.

Sample Input
============
5
.....
  #  
#    

    .

Sample Output
=============
  .  
. #  
#    
    .
 . ..
"""

def run(grid):
  """
  for c in range(0, len(grid)):
    for r in range(0, len(grid) - 1):
      if grid[r + 1][c] == ' ':
        grid[r + 1][c] = grid[r][c]
        grid[r][c] = ' '
      elif grid[r + 1][c] == '#':
        break
      else:
        pass

  """
  for c in reversed(xrange(len(grid))):
    rc = len(grid) - 1
    for r in reversed(xrange(len(grid))):
      if grid[r][c] == '#':
        rc = r - 1
      elif grid[r][c] == '.' and rc is not r:
        grid[rc][c] = grid[r][c]
        grid[r][c] = ' ';
        rc -= 1
      elif grid[r][c] == '.':
        rc -= 1

  return grid
        

def _print(grid):
  print '\n'.join([ ''.join(grid[c]) for c in range(0, len(grid)) ])


parse = lambda l: list(l)

if __name__ == '__main__':
  """
  n = int(raw_input())
  grid = []
  for i in range(0, n):
    grid.append(parse(raw_input()))
  """

  grid = [
    [ '.', '.', '.', '.', '.' ],
    [ ' ', ' ', '#', '.', ' ' ],
    [ '#', ' ', ' ', ' ', ' ' ],
    [ ' ', ' ', ' ', ' ', ' ' ],
    [ ' ', ' ', ' ', ' ', '.' ]
  ]
  """
  grid = [
    [ '.', '#', '.' ],
    [ '.', ' ', '.' ],
    [ '.', ' ', '.' ]
  ]
  """
  """
  grid = [
    [ '.', '.', '.', '.', '.' ],
    [ '.', '.', '.', '.', '.' ],
    [ ' ', ' ', '#', ' ', ' ' ],
    [ ' ', '#', ' ', '#', ' ' ],
    [ '.', ' ', ' ', ' ', '.' ]
  ]
  """

  _print(run(grid))
  

