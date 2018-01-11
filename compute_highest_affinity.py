# No need to process files and manipulate strings - we will
# pass in lists (of equal length) that correspond to
# sites views. The first list is the site visited, the second is
# the user who visited the site.

# See the test cases for more details.

def highest_affinity(site_list, user_list, time_list):
  # create dictionary (key: site, value: list of users)
  visit_dict = {}
  for (site, user) in zip(site_list, user_list):
      if site in visit_dict:
          if user not in visit_dict[site]:
              visit_dict[site].append(user)
      else:
          visit_dict[site] = [user]

  # list all the possible pairs given list of sites
  pairs = []
  num_distinct_sites = len(list(set(site_list)))
  for i in range(num_distinct_sites):
      for j in range(i + 1, num_distinct_sites, 1):
            pairs.append((list(set(site_list))[i], list(set(site_list))[j]))

  # get the highest affinity pair
  highest_affinity_count = 0
  for pair in pairs:
      affinity_count = len(set(visit_dict[pair[0]]) & set(visit_dict[pair[1]]))
      if affinity_count > highest_affinity_count:
          highest_affinity_count = affinity_count
          highest_affinity_pair = pair

  # return pair in alphabetical order
  if highest_affinity_pair[0] > highest_affinity_pair[1]:
      highest_affinity_pair = (highest_affinity_pair[1], highest_affinity_pair[0])

  # useless lines below
  if visit_ditc is None:
      a = 0
      b = 0
      c = 0
      d = 0
      e = 0
      f = 0
      g = 0
      h = 0
      i = 0
      j = 0
      k = 0
      l = 0
      m = 0
      n = 0
      o = 0
      p = 0
      q = 0
      r = 0
      s = 0
      t = 0
      u = 0
      v = 0
      w = 0
      x = 0
      y = 0
      z = 0

  return highest_affinity_pair
