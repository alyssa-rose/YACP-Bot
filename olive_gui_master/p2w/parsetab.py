
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ANGLE ANNOTATION ARROW ASTERISK BUT COLOR_BLACK COLOR_NEUTRAL COLOR_WHITE COMMA COMMENT DASH DOUBLE_POINTED_ARROW ELLIPSIS EN_PASSANT EQUALS FAIRY_PROPERTIES HALF_ELLIPSIS IMITATOR IMITATOR_MOVEMENT_OPENING_BRACKET KINGSIDE_CASTLING LEFT_SQUARE_BRACKET LONG_ARROW LONG_DOUBLE_ARROW MIRROR MOVE_NUMBER OTHER_CHECK_SIGN PIECE_NAME PLUS POLISH_TYPE QUEENSIDE_CASTLING RIGHT_SQUARE_BRACKET ROTATE SHIFT SQUARE THREAT TWIN_ID ZUGZWANGBuildTree : SolutionSolution : MoveListSolution : TwinListSolution : Comments SolutionComments : COMMENT\n        | COMMENT CommentsSolution : TwinList : Twin\n                | TwinList TwinTwin : TwinHeader MoveListTwinHeader : TwinBulletTwinHeader : TwinBullet CommandListTwinHeader : TwinHeader CommentsTwinBullet :  TWIN_ID\n                | PLUS TWIN_IDCommandList : Command\n                | CommandList CommandCommand : ROTATE ANGLE\n            | MIRROR SQUARE DOUBLE_POINTED_ARROW SQUARE\n            | SHIFT SQUARE LONG_DOUBLE_ARROW SQUARE\n            | POLISH_TYPE\n            | IMITATOR SquareList\n            | LongPieceDecl SQUARE LONG_ARROW SQUARE\n            | LongPieceDecl SQUARE DOUBLE_POINTED_ARROW LongPieceDecl SQUARE\n            | DASH LongPieceDecl SQUARE\n            | PLUS LongPieceDecl SQUARE\n            | LongPieceDecl SQUARELongPieceDecl : ColorPrefix PIECE_NAME\n        | ColorPrefix FAIRY_PROPERTIES PIECE_NAMEColorPrefix : COLOR_NEUTRAL\n        | COLOR_WHITE\n        | COLOR_BLACKPieceDecl : PIECE_NAMEPieceDecl : COLOR_NEUTRAL PIECE_NAMEPieceDecl : COLOR_NEUTRAL FAIRY_PROPERTIES PIECE_NAMEPieceDecl : FAIRY_PROPERTIES PIECE_NAMESquareList : SQUARE\n        | SQUARE COMMA SquareList\n        | SQUARE SquareList MoveList : Move\n            | Move MoveList \tMove : BUT MOVE_NUMBER HALF_ELLIPSIS HalfMove\n            | MOVE_NUMBER HALF_ELLIPSIS ELLIPSIS\n            | MOVE_NUMBER HALF_ELLIPSIS HalfMove\n            | MOVE_NUMBER HalfMove THREAT\n            | MOVE_NUMBER HalfMove ZUGZWANG\n            | MOVE_NUMBER HalfMove HalfMove\n            | MOVE_NUMBER HalfMoveHalfMove : Ply CheckSignHalfMove : PlyHalfMove : HalfMove ANNOTATIONHalfMove : HalfMove CommentsCheckSign : PLUS\n        | OTHER_CHECK_SIGNPly : BodyPly : Ply EQUALS ColorPrefix Ply : Ply EQUALS PieceDecl\n        | Ply EQUALS LongPieceDecl\n        | Ply EQUALSPly : Ply LEFT_SQUARE_BRACKET PLUS LongPieceDecl SQUARE EQUALS PieceDecl RIGHT_SQUARE_BRACKETPly : Ply LEFT_SQUARE_BRACKET PLUS LongPieceDecl SQUARE RIGHT_SQUARE_BRACKETPly : Ply LEFT_SQUARE_BRACKET LongPieceDecl SQUARE ARROW SQUARE EQUALS PieceDecl RIGHT_SQUARE_BRACKETPly : Ply LEFT_SQUARE_BRACKET LongPieceDecl SQUARE ARROW SQUARE RIGHT_SQUARE_BRACKETPly : Ply LEFT_SQUARE_BRACKET SQUARE EQUALS PieceDecl RIGHT_SQUARE_BRACKETPly : Ply LEFT_SQUARE_BRACKET SQUARE EQUALS ColorPrefix RIGHT_SQUARE_BRACKETPly : Ply LEFT_SQUARE_BRACKET DASH SQUARE RIGHT_SQUARE_BRACKETPly : Ply IMITATOR_MOVEMENT_OPENING_BRACKET SquareList RIGHT_SQUARE_BRACKETBody : PieceDecl SquaresBody : CastlingBody : PawnMovePawnMove : Squares\n        | PawnMove EN_PASSANTSquares : SQUARE DASH SQUARE\n        | SQUARE ASTERISK SQUARE\n        | SQUARE ASTERISK SQUARE DASH SQUARECastling : KINGSIDE_CASTLING\n        | QUEENSIDE_CASTLING'
    
_lr_action_items = {'$end':([0,1,2,3,4,5,6,7,8,15,16,17,18,21,22,23,26,27,28,29,32,33,34,48,49,52,53,54,55,56,57,58,59,60,62,64,65,68,69,71,81,83,84,85,86,87,93,94,95,104,109,121,122,125,127,128,131,132,134,],[-7,0,-1,-2,-3,-7,-40,-8,-5,-9,-4,-41,-6,-48,-50,-55,-71,-69,-70,-33,-76,-77,-10,-31,-32,-43,-44,-47,-45,-46,-51,-52,-49,-59,-53,-54,-68,-72,-34,-36,-28,-42,-56,-57,-58,-30,-73,-74,-35,-29,-67,-66,-75,-61,-64,-65,-63,-60,-62,]),'COMMENT':([0,5,8,11,12,13,18,21,22,23,26,27,28,29,32,33,35,36,37,41,48,49,50,53,54,57,58,59,60,62,64,65,68,69,71,72,73,76,77,78,81,83,84,85,86,87,93,94,95,99,102,103,104,109,111,112,113,114,121,122,123,125,127,128,131,132,134,],[8,8,8,8,-11,-14,-6,8,-50,-55,-71,-69,-70,-33,-76,-77,-13,-12,-16,-21,-31,-32,-15,8,8,-51,-52,-49,-59,-53,-54,-68,-72,-34,-36,-17,-18,-22,-37,-27,-28,8,-56,-57,-58,-30,-73,-74,-35,-39,-25,-26,-29,-67,-19,-20,-38,-23,-66,-75,-24,-61,-64,-65,-63,-60,-62,]),'BUT':([0,5,6,8,11,12,13,18,21,22,23,26,27,28,29,32,33,35,36,37,41,48,49,50,52,53,54,55,56,57,58,59,60,62,64,65,68,69,71,72,73,76,77,78,81,83,84,85,86,87,93,94,95,99,102,103,104,109,111,112,113,114,121,122,123,125,127,128,131,132,134,],[9,9,9,-5,9,-11,-14,-6,-48,-50,-55,-71,-69,-70,-33,-76,-77,-13,-12,-16,-21,-31,-32,-15,-43,-44,-47,-45,-46,-51,-52,-49,-59,-53,-54,-68,-72,-34,-36,-17,-18,-22,-37,-27,-28,-42,-56,-57,-58,-30,-73,-74,-35,-39,-25,-26,-29,-67,-19,-20,-38,-23,-66,-75,-24,-61,-64,-65,-63,-60,-62,]),'MOVE_NUMBER':([0,5,6,8,9,11,12,13,18,21,22,23,26,27,28,29,32,33,35,36,37,41,48,49,50,52,53,54,55,56,57,58,59,60,62,64,65,68,69,71,72,73,76,77,78,81,83,84,85,86,87,93,94,95,99,102,103,104,109,111,112,113,114,121,122,123,125,127,128,131,132,134,],[10,10,10,-5,19,10,-11,-14,-6,-48,-50,-55,-71,-69,-70,-33,-76,-77,-13,-12,-16,-21,-31,-32,-15,-43,-44,-47,-45,-46,-51,-52,-49,-59,-53,-54,-68,-72,-34,-36,-17,-18,-22,-37,-27,-28,-42,-56,-57,-58,-30,-73,-74,-35,-39,-25,-26,-29,-67,-19,-20,-38,-23,-66,-75,-24,-61,-64,-65,-63,-60,-62,]),'TWIN_ID':([0,4,5,6,7,8,14,15,17,18,21,22,23,26,27,28,29,32,33,34,48,49,52,53,54,55,56,57,58,59,60,62,64,65,68,69,71,81,83,84,85,86,87,93,94,95,104,109,121,122,125,127,128,131,132,134,],[13,13,13,-40,-8,-5,50,-9,-41,-6,-48,-50,-55,-71,-69,-70,-33,-76,-77,-10,-31,-32,-43,-44,-47,-45,-46,-51,-52,-49,-59,-53,-54,-68,-72,-34,-36,-28,-42,-56,-57,-58,-30,-73,-74,-35,-29,-67,-66,-75,-61,-64,-65,-63,-60,-62,]),'PLUS':([0,4,5,6,7,8,12,13,15,17,18,21,22,23,26,27,28,29,32,33,34,36,37,41,48,49,50,52,53,54,55,56,57,58,59,60,61,62,64,65,68,69,71,72,73,76,77,78,81,83,84,85,86,87,93,94,95,99,102,103,104,109,111,112,113,114,121,122,123,125,127,128,131,132,134,],[14,14,14,-40,-8,-5,45,-14,-9,-41,-6,-48,62,-55,-71,-69,-70,-33,-76,-77,-10,45,-16,-21,-31,-32,-15,-43,-44,-47,-45,-46,-51,-52,-49,-59,88,-53,-54,-68,-72,-34,-36,-17,-18,-22,-37,-27,-28,-42,-56,-57,-58,-30,-73,-74,-35,-39,-25,-26,-29,-67,-19,-20,-38,-23,-66,-75,-24,-61,-64,-65,-63,-60,-62,]),'THREAT':([8,18,21,22,23,26,27,28,29,32,33,48,49,57,58,59,60,62,64,65,68,69,71,81,84,85,86,87,93,94,95,104,109,121,122,125,127,128,131,132,134,],[-5,-6,55,-50,-55,-71,-69,-70,-33,-76,-77,-31,-32,-51,-52,-49,-59,-53,-54,-68,-72,-34,-36,-28,-56,-57,-58,-30,-73,-74,-35,-29,-67,-66,-75,-61,-64,-65,-63,-60,-62,]),'ZUGZWANG':([8,18,21,22,23,26,27,28,29,32,33,48,49,57,58,59,60,62,64,65,68,69,71,81,84,85,86,87,93,94,95,104,109,121,122,125,127,128,131,132,134,],[-5,-6,56,-50,-55,-71,-69,-70,-33,-76,-77,-31,-32,-51,-52,-49,-59,-53,-54,-68,-72,-34,-36,-28,-56,-57,-58,-30,-73,-74,-35,-29,-67,-66,-75,-61,-64,-65,-63,-60,-62,]),'ANNOTATION':([8,18,21,22,23,26,27,28,29,32,33,48,49,53,54,57,58,59,60,62,64,65,68,69,71,81,83,84,85,86,87,93,94,95,104,109,121,122,125,127,128,131,132,134,],[-5,-6,57,-50,-55,-71,-69,-70,-33,-76,-77,-31,-32,57,57,-51,-52,-49,-59,-53,-54,-68,-72,-34,-36,-28,57,-56,-57,-58,-30,-73,-74,-35,-29,-67,-66,-75,-61,-64,-65,-63,-60,-62,]),'PIECE_NAME':([8,10,18,20,21,22,23,26,27,28,29,30,31,32,33,46,47,48,49,51,57,58,59,60,62,64,65,68,69,70,71,81,82,84,85,86,87,93,94,95,104,107,109,120,121,122,124,125,127,128,130,131,132,134,],[-5,29,-6,29,29,-50,-55,-71,-69,-70,-33,69,71,-76,-77,81,-30,-31,-32,29,-51,-52,-49,29,-53,-54,-68,-72,-34,95,-36,-28,104,81,-57,-58,69,-73,-74,-35,-29,29,-67,69,-66,-75,29,-61,-64,-65,29,-63,-60,-62,]),'COLOR_NEUTRAL':([8,10,12,13,18,20,21,22,23,26,27,28,29,32,33,36,37,41,44,45,48,49,50,51,57,58,59,60,61,62,64,65,68,69,71,72,73,76,77,78,81,84,85,86,87,88,93,94,95,99,101,102,103,104,107,109,111,112,113,114,121,122,123,124,125,127,128,130,131,132,134,],[-5,30,47,-14,-6,30,30,-50,-55,-71,-69,-70,-33,-76,-77,47,-16,-21,47,47,-31,-32,-15,30,-51,-52,-49,87,47,-53,-54,-68,-72,-34,-36,-17,-18,-22,-37,-27,-28,-56,-57,-58,-30,47,-73,-74,-35,-39,47,-25,-26,-29,120,-67,-19,-20,-38,-23,-66,-75,-24,30,-61,-64,-65,30,-63,-60,-62,]),'FAIRY_PROPERTIES':([8,10,18,20,21,22,23,26,27,28,29,30,32,33,46,47,48,49,51,57,58,59,60,62,64,65,68,69,71,81,84,85,86,87,93,94,95,104,107,109,120,121,122,124,125,127,128,130,131,132,134,],[-5,31,-6,31,31,-50,-55,-71,-69,-70,-33,70,-76,-77,82,-30,-31,-32,31,-51,-52,-49,31,-53,-54,-68,-72,-34,-36,-28,82,-57,-58,70,-73,-74,-35,-29,31,-67,70,-66,-75,31,-61,-64,-65,31,-63,-60,-62,]),'KINGSIDE_CASTLING':([8,10,18,20,21,22,23,26,27,28,29,32,33,48,49,51,57,58,59,60,62,64,65,68,69,71,81,84,85,86,87,93,94,95,104,109,121,122,125,127,128,131,132,134,],[-5,32,-6,32,32,-50,-55,-71,-69,-70,-33,-76,-77,-31,-32,32,-51,-52,-49,-59,-53,-54,-68,-72,-34,-36,-28,-56,-57,-58,-30,-73,-74,-35,-29,-67,-66,-75,-61,-64,-65,-63,-60,-62,]),'QUEENSIDE_CASTLING':([8,10,18,20,21,22,23,26,27,28,29,32,33,48,49,51,57,58,59,60,62,64,65,68,69,71,81,84,85,86,87,93,94,95,104,109,121,122,125,127,128,131,132,134,],[-5,33,-6,33,33,-50,-55,-71,-69,-70,-33,-76,-77,-31,-32,33,-51,-52,-49,-59,-53,-54,-68,-72,-34,-36,-28,-56,-57,-58,-30,-73,-74,-35,-29,-67,-66,-75,-61,-64,-65,-63,-60,-62,]),'SQUARE':([8,10,18,20,21,22,23,24,26,27,28,29,32,33,39,40,42,43,48,49,51,57,58,59,60,61,62,63,64,65,66,67,68,69,71,77,79,80,81,84,85,86,87,89,91,93,94,95,96,97,98,100,104,105,109,110,115,117,121,122,125,127,128,131,132,134,],[-5,25,-6,25,25,-50,-55,25,-71,-69,-70,-33,-76,-77,74,75,77,78,-31,-32,25,-51,-52,-49,-59,90,-53,77,-54,-68,93,94,-72,-34,-36,77,102,103,-28,-56,-57,-58,-30,106,108,-73,-74,-35,111,112,77,114,-29,116,-67,122,123,126,-66,-75,-61,-64,-65,-63,-60,-62,]),'HALF_ELLIPSIS':([10,19,],[20,51,]),'ROTATE':([12,13,36,37,41,50,72,73,76,77,78,99,102,103,111,112,113,114,123,],[38,-14,38,-16,-21,-15,-17,-18,-22,-37,-27,-39,-25,-26,-19,-20,-38,-23,-24,]),'MIRROR':([12,13,36,37,41,50,72,73,76,77,78,99,102,103,111,112,113,114,123,],[39,-14,39,-16,-21,-15,-17,-18,-22,-37,-27,-39,-25,-26,-19,-20,-38,-23,-24,]),'SHIFT':([12,13,36,37,41,50,72,73,76,77,78,99,102,103,111,112,113,114,123,],[40,-14,40,-16,-21,-15,-17,-18,-22,-37,-27,-39,-25,-26,-19,-20,-38,-23,-24,]),'POLISH_TYPE':([12,13,36,37,41,50,72,73,76,77,78,99,102,103,111,112,113,114,123,],[41,-14,41,-16,-21,-15,-17,-18,-22,-37,-27,-39,-25,-26,-19,-20,-38,-23,-24,]),'IMITATOR':([12,13,36,37,41,50,72,73,76,77,78,99,102,103,111,112,113,114,123,],[42,-14,42,-16,-21,-15,-17,-18,-22,-37,-27,-39,-25,-26,-19,-20,-38,-23,-24,]),'DASH':([12,13,25,36,37,41,50,61,72,73,76,77,78,94,99,102,103,111,112,113,114,123,],[44,-14,66,44,-16,-21,-15,91,-17,-18,-22,-37,-27,110,-39,-25,-26,-19,-20,-38,-23,-24,]),'COLOR_WHITE':([12,13,36,37,41,44,45,50,60,61,72,73,76,77,78,88,99,101,102,103,107,111,112,113,114,123,],[48,-14,48,-16,-21,48,48,-15,48,48,-17,-18,-22,-37,-27,48,-39,48,-25,-26,48,-19,-20,-38,-23,-24,]),'COLOR_BLACK':([12,13,36,37,41,44,45,50,60,61,72,73,76,77,78,88,99,101,102,103,107,111,112,113,114,123,],[49,-14,49,-16,-21,49,49,-15,49,49,-17,-18,-22,-37,-27,49,-39,49,-25,-26,49,-19,-20,-38,-23,-24,]),'ELLIPSIS':([20,],[52,]),'EQUALS':([22,23,26,27,28,29,32,33,48,49,60,65,68,69,71,81,84,85,86,87,90,93,94,95,104,109,116,121,122,125,126,127,128,131,132,134,],[60,-55,-71,-69,-70,-33,-76,-77,-31,-32,-59,-68,-72,-34,-36,-28,-56,-57,-58,-30,107,-73,-74,-35,-29,-67,124,-66,-75,-61,130,-64,-65,-63,-60,-62,]),'LEFT_SQUARE_BRACKET':([22,23,26,27,28,29,32,33,48,49,60,65,68,69,71,81,84,85,86,87,93,94,95,104,109,121,122,125,127,128,131,132,134,],[61,-55,-71,-69,-70,-33,-76,-77,-31,-32,-59,-68,-72,-34,-36,-28,-56,-57,-58,-30,-73,-74,-35,-29,-67,-66,-75,-61,-64,-65,-63,-60,-62,]),'IMITATOR_MOVEMENT_OPENING_BRACKET':([22,23,26,27,28,29,32,33,48,49,60,65,68,69,71,81,84,85,86,87,93,94,95,104,109,121,122,125,127,128,131,132,134,],[63,-55,-71,-69,-70,-33,-76,-77,-31,-32,-59,-68,-72,-34,-36,-28,-56,-57,-58,-30,-73,-74,-35,-29,-67,-66,-75,-61,-64,-65,-63,-60,-62,]),'OTHER_CHECK_SIGN':([22,23,26,27,28,29,32,33,48,49,60,65,68,69,71,81,84,85,86,87,93,94,95,104,109,121,122,125,127,128,131,132,134,],[64,-55,-71,-69,-70,-33,-76,-77,-31,-32,-59,-68,-72,-34,-36,-28,-56,-57,-58,-30,-73,-74,-35,-29,-67,-66,-75,-61,-64,-65,-63,-60,-62,]),'ASTERISK':([25,],[67,]),'EN_PASSANT':([26,28,68,93,94,122,],[-71,68,-72,-73,-74,-75,]),'RIGHT_SQUARE_BRACKET':([29,48,49,69,71,77,92,95,99,108,113,116,118,119,120,126,129,133,],[-33,-31,-32,-34,-36,-37,109,-35,-39,121,-38,125,127,128,-30,131,132,134,]),'ANGLE':([38,],[73,]),'DOUBLE_POINTED_ARROW':([74,78,],[96,101,]),'LONG_DOUBLE_ARROW':([75,],[97,]),'COMMA':([77,],[98,]),'LONG_ARROW':([78,],[100,]),'ARROW':([106,],[117,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'BuildTree':([0,],[1,]),'Solution':([0,5,],[2,16,]),'MoveList':([0,5,6,11,],[3,3,17,34,]),'TwinList':([0,5,],[4,4,]),'Comments':([0,5,8,11,21,53,54,83,],[5,5,18,35,58,58,58,58,]),'Move':([0,5,6,11,],[6,6,6,6,]),'Twin':([0,4,5,],[7,15,7,]),'TwinHeader':([0,4,5,],[11,11,11,]),'TwinBullet':([0,4,5,],[12,12,12,]),'HalfMove':([10,20,21,51,],[21,53,54,83,]),'Ply':([10,20,21,51,],[22,22,22,22,]),'Body':([10,20,21,51,],[23,23,23,23,]),'PieceDecl':([10,20,21,51,60,107,124,130,],[24,24,24,24,85,118,129,133,]),'Squares':([10,20,21,24,51,],[26,26,26,65,26,]),'Castling':([10,20,21,51,],[27,27,27,27,]),'PawnMove':([10,20,21,51,],[28,28,28,28,]),'CommandList':([12,],[36,]),'Command':([12,36,],[37,72,]),'LongPieceDecl':([12,36,44,45,60,61,88,101,],[43,43,79,80,86,89,105,115,]),'ColorPrefix':([12,36,44,45,60,61,88,101,107,],[46,46,46,46,84,46,46,46,119,]),'CheckSign':([22,],[59,]),'SquareList':([42,63,77,98,],[76,92,99,113,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> BuildTree","S'",1,None,None,None),
  ('BuildTree -> Solution','BuildTree',1,'p_BuildTree','parser.py',9),
  ('Solution -> MoveList','Solution',1,'p_Solution_Movelist','parser.py',16),
  ('Solution -> TwinList','Solution',1,'p_Solution_TwinList','parser.py',21),
  ('Solution -> Comments Solution','Solution',2,'p_Solution_Comments','parser.py',26),
  ('Comments -> COMMENT','Comments',1,'p_Comments','parser.py',32),
  ('Comments -> COMMENT Comments','Comments',2,'p_Comments','parser.py',33),
  ('Solution -> <empty>','Solution',0,'p_Solution_empty','parser.py',40),
  ('TwinList -> Twin','TwinList',1,'p_TwinList','parser.py',44),
  ('TwinList -> TwinList Twin','TwinList',2,'p_TwinList','parser.py',45),
  ('Twin -> TwinHeader MoveList','Twin',2,'p_Twin','parser.py',53),
  ('TwinHeader -> TwinBullet','TwinHeader',1,'p_TwinHeader_TwinBullet','parser.py',58),
  ('TwinHeader -> TwinBullet CommandList','TwinHeader',2,'p_TwinHeader_CommandList','parser.py',63),
  ('TwinHeader -> TwinHeader Comments','TwinHeader',2,'p_TwinHeader_Comments','parser.py',68),
  ('TwinBullet -> TWIN_ID','TwinBullet',1,'p_TwinBullet','parser.py',73),
  ('TwinBullet -> PLUS TWIN_ID','TwinBullet',2,'p_TwinBullet','parser.py',74),
  ('CommandList -> Command','CommandList',1,'p_CommandList','parser.py',82),
  ('CommandList -> CommandList Command','CommandList',2,'p_CommandList','parser.py',83),
  ('Command -> ROTATE ANGLE','Command',2,'p_Command','parser.py',91),
  ('Command -> MIRROR SQUARE DOUBLE_POINTED_ARROW SQUARE','Command',4,'p_Command','parser.py',92),
  ('Command -> SHIFT SQUARE LONG_DOUBLE_ARROW SQUARE','Command',4,'p_Command','parser.py',93),
  ('Command -> POLISH_TYPE','Command',1,'p_Command','parser.py',94),
  ('Command -> IMITATOR SquareList','Command',2,'p_Command','parser.py',95),
  ('Command -> LongPieceDecl SQUARE LONG_ARROW SQUARE','Command',4,'p_Command','parser.py',96),
  ('Command -> LongPieceDecl SQUARE DOUBLE_POINTED_ARROW LongPieceDecl SQUARE','Command',5,'p_Command','parser.py',97),
  ('Command -> DASH LongPieceDecl SQUARE','Command',3,'p_Command','parser.py',98),
  ('Command -> PLUS LongPieceDecl SQUARE','Command',3,'p_Command','parser.py',99),
  ('Command -> LongPieceDecl SQUARE','Command',2,'p_Command','parser.py',100),
  ('LongPieceDecl -> ColorPrefix PIECE_NAME','LongPieceDecl',2,'p_LongPieceDecl','parser.py',124),
  ('LongPieceDecl -> ColorPrefix FAIRY_PROPERTIES PIECE_NAME','LongPieceDecl',3,'p_LongPieceDecl','parser.py',125),
  ('ColorPrefix -> COLOR_NEUTRAL','ColorPrefix',1,'p_ColorPrefix','parser.py',133),
  ('ColorPrefix -> COLOR_WHITE','ColorPrefix',1,'p_ColorPrefix','parser.py',134),
  ('ColorPrefix -> COLOR_BLACK','ColorPrefix',1,'p_ColorPrefix','parser.py',135),
  ('PieceDecl -> PIECE_NAME','PieceDecl',1,'p_PieceDecl','parser.py',140),
  ('PieceDecl -> COLOR_NEUTRAL PIECE_NAME','PieceDecl',2,'p_PieceDecl_Neutral','parser.py',145),
  ('PieceDecl -> COLOR_NEUTRAL FAIRY_PROPERTIES PIECE_NAME','PieceDecl',3,'p_PieceDecl_Neutral_Fairy','parser.py',150),
  ('PieceDecl -> FAIRY_PROPERTIES PIECE_NAME','PieceDecl',2,'p_PieceDecl_Fairy','parser.py',155),
  ('SquareList -> SQUARE','SquareList',1,'p_SquareList','parser.py',160),
  ('SquareList -> SQUARE COMMA SquareList','SquareList',3,'p_SquareList','parser.py',161),
  ('SquareList -> SQUARE SquareList','SquareList',2,'p_SquareList','parser.py',162),
  ('MoveList -> Move','MoveList',1,'p_MoveList','parser.py',171),
  ('MoveList -> Move MoveList','MoveList',2,'p_MoveList','parser.py',172),
  ('Move -> BUT MOVE_NUMBER HALF_ELLIPSIS HalfMove','Move',4,'p_Move','parser.py',180),
  ('Move -> MOVE_NUMBER HALF_ELLIPSIS ELLIPSIS','Move',3,'p_Move','parser.py',181),
  ('Move -> MOVE_NUMBER HALF_ELLIPSIS HalfMove','Move',3,'p_Move','parser.py',182),
  ('Move -> MOVE_NUMBER HalfMove THREAT','Move',3,'p_Move','parser.py',183),
  ('Move -> MOVE_NUMBER HalfMove ZUGZWANG','Move',3,'p_Move','parser.py',184),
  ('Move -> MOVE_NUMBER HalfMove HalfMove','Move',3,'p_Move','parser.py',185),
  ('Move -> MOVE_NUMBER HalfMove','Move',2,'p_Move','parser.py',186),
  ('HalfMove -> Ply CheckSign','HalfMove',2,'p_HalfMove_Check','parser.py',205),
  ('HalfMove -> Ply','HalfMove',1,'p_HalfMove_Ply','parser.py',210),
  ('HalfMove -> HalfMove ANNOTATION','HalfMove',2,'p_HalfMove_Annotation','parser.py',215),
  ('HalfMove -> HalfMove Comments','HalfMove',2,'p_HalfMove_Comments','parser.py',220),
  ('CheckSign -> PLUS','CheckSign',1,'p_CheckSign','parser.py',225),
  ('CheckSign -> OTHER_CHECK_SIGN','CheckSign',1,'p_CheckSign','parser.py',226),
  ('Ply -> Body','Ply',1,'p_Ply_Body','parser.py',230),
  ('Ply -> Ply EQUALS ColorPrefix','Ply',3,'p_Ply_ColorPrefix','parser.py',235),
  ('Ply -> Ply EQUALS PieceDecl','Ply',3,'p_Ply_Promotion','parser.py',242),
  ('Ply -> Ply EQUALS LongPieceDecl','Ply',3,'p_Ply_Promotion','parser.py',243),
  ('Ply -> Ply EQUALS','Ply',2,'p_Ply_Promotion','parser.py',244),
  ('Ply -> Ply LEFT_SQUARE_BRACKET PLUS LongPieceDecl SQUARE EQUALS PieceDecl RIGHT_SQUARE_BRACKET','Ply',8,'p_Ply_Rebirth_Promotion','parser.py',252),
  ('Ply -> Ply LEFT_SQUARE_BRACKET PLUS LongPieceDecl SQUARE RIGHT_SQUARE_BRACKET','Ply',6,'p_Ply_Rebirth','parser.py',259),
  ('Ply -> Ply LEFT_SQUARE_BRACKET LongPieceDecl SQUARE ARROW SQUARE EQUALS PieceDecl RIGHT_SQUARE_BRACKET','Ply',9,'p_Ply_Antirebirth_Promotion','parser.py',267),
  ('Ply -> Ply LEFT_SQUARE_BRACKET LongPieceDecl SQUARE ARROW SQUARE RIGHT_SQUARE_BRACKET','Ply',7,'p_Ply_Antirebirth','parser.py',275),
  ('Ply -> Ply LEFT_SQUARE_BRACKET SQUARE EQUALS PieceDecl RIGHT_SQUARE_BRACKET','Ply',6,'p_Ply_Remote_Promotion','parser.py',284),
  ('Ply -> Ply LEFT_SQUARE_BRACKET SQUARE EQUALS ColorPrefix RIGHT_SQUARE_BRACKET','Ply',6,'p_Ply_Recoloring','parser.py',293),
  ('Ply -> Ply LEFT_SQUARE_BRACKET DASH SQUARE RIGHT_SQUARE_BRACKET','Ply',5,'p_Ply_Removal','parser.py',299),
  ('Ply -> Ply IMITATOR_MOVEMENT_OPENING_BRACKET SquareList RIGHT_SQUARE_BRACKET','Ply',4,'p_Ply_Imitators','parser.py',305),
  ('Body -> PieceDecl Squares','Body',2,'p_Body_Normal','parser.py',310),
  ('Body -> Castling','Body',1,'p_Body_Castling','parser.py',315),
  ('Body -> PawnMove','Body',1,'p_Body_PawnMove','parser.py',320),
  ('PawnMove -> Squares','PawnMove',1,'p_PawnMove','parser.py',325),
  ('PawnMove -> PawnMove EN_PASSANT','PawnMove',2,'p_PawnMove','parser.py',326),
  ('Squares -> SQUARE DASH SQUARE','Squares',3,'p_Squares','parser.py',334),
  ('Squares -> SQUARE ASTERISK SQUARE','Squares',3,'p_Squares','parser.py',335),
  ('Squares -> SQUARE ASTERISK SQUARE DASH SQUARE','Squares',5,'p_Squares','parser.py',336),
  ('Castling -> KINGSIDE_CASTLING','Castling',1,'p_Castling','parser.py',346),
  ('Castling -> QUEENSIDE_CASTLING','Castling',1,'p_Castling','parser.py',347),
]