import sys,tempfile,unittest
from pathlib import Path
from PIL import Image
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
from index_images import index
class IndexTests(unittest.TestCase):
 def test_exact_duplicates_are_suggestions(self):
  with tempfile.TemporaryDirectory() as folder:
   p=Path(folder);Image.new("RGB",(16,16),"red").save(p/"a.png");(p/"b.png").write_bytes((p/"a.png").read_bytes());r=index(folder)
   self.assertEqual(len(r["images"]),2);self.assertTrue(r["duplicateSuggestions"][0]["exact"]);self.assertEqual(r["duplicateSuggestions"][0]["status"],"needs-review")
 def test_distinct_patterns_not_suggested_at_zero_distance(self):
  with tempfile.TemporaryDirectory() as folder:
   p=Path(folder)
   for name,reverse in [("a",False),("b",True)]:
    im=Image.new("L",(9,8));im.putdata([x*28 if not reverse else 224-x*28 for y in range(8) for x in range(9)]);im.save(p/(name+".png"))
   self.assertEqual(index(folder,0)["duplicateSuggestions"],[])
