from tqdm import tqdm
import numpy as np
import torch
#from tensorboardX import SummaryWriter
#summary = SummaryWriter()
#import wandb

def train(epoch, model, optimizer, train_loader, save_step, save_ckpt_path, train_step = 0):
    losses = []
    train_start_index = train_step+1 if train_step != 0 else 0
    total_train_step = len(train_loader)
    model.train()
    total_loss = 0
    total_accuracy = 0
    total_matthews_coeff = 0
    with tqdm(total= total_train_step, desc=f"Train({epoch})") as pbar:
        pbar.update(train_step)
        for i, data in enumerate(train_loader, train_start_index):
            optimizer.zero_grad()

            '''
            inputs = {'input_ids': batch[0],
                      'attention_mask': batch[1],
                      'bias_labels': batch[3],
                      'hate_labels': batch[4]}
            if self.args.model_type != 'distilkobert':
              inputs['token_type_ids'] = batch[2]
            '''
            inputs = {'input_ids': data['input_ids'],
                      'attention_mask': data['attention_mask'],
                      'labels': data['labels']
                      }
            outputs = model(**inputs)

            loss = outputs[0]

            losses.append(loss.item())
            total_loss += loss.item()
            loss.backward()
            optimizer.step()

            pbar.update(1)
            pbar.set_postfix_str(f"Loss: {loss.item():.3f} ({np.mean(losses):.3f})")

            if i >= total_train_step or i % save_step == 0:
                #summary.add_scalar('loss', loss.item(), i)
                torch.save({
                    'epoch': epoch,  # 현재 학습 epoch
                    'model_state_dict': model.state_dict(),  # 모델 저장
                    'optimizer_state_dict': optimizer.state_dict(),  # 옵티마이저 저장
                    'loss': loss.item(),  # Loss 저장
                    'train_step': i,  # 현재 진행한 학습
                    'total_train_step': len(train_loader)  # 현재 epoch에 학습 할 총 train step
                }, save_ckpt_path)

    return np.mean(losses)

def train_one_epoch(model,train_loader,optimizer,scheduler,loss_function, train_step = 0):
    model.train()
    train_start_index = train_step + 1 if train_step != 0 else 0
    total_train_step = len(train_loader)
    total_loss = 0
    total_accuracy = 0
    total_matthews_coeff = 0
    for i, data in enumerate(train_loader, train_start_index):
        loss, accuracy, matthews_coeff = train(1, model, optimizer, data, scheduler, loss_function)
        scheduler.step()

        total_loss += loss
        total_accuracy += accuracy
        total_matthews_coeff += matthews_coeff

    return total_loss / len(train_loader), total_accuracy / len(train_loader), total_matthews_coeff / len(train_loader)


def val_one_step(model,data,loss_function):
    correct_prediction = 0


def val_train(model,train_loader,optimizer,loss_function, train_step = 0):
    model.eval()
    train_start_index = train_step + 1 if train_step != 0 else 0
    total_train_step = len(train_loader)
    total_loss = 0
    total_accuracy = 0
    total_matthews_coeff = 0
    for i, data in enumerate(train_loader, train_start_index):
        optimizer.zero_grad()
        loss, accuracy, matthews_coeff = val_one_step(model, data, loss_function)
        total_loss += loss
        total_accuracy += accuracy
        total_matthews_coeff += matthews_coeff

        return total_loss / len(train_loader), total_accuracy / len(train_loader), total_matthews_coeff / len(train_loader)